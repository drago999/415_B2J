from neo4j import GraphDatabase

# Define the connection details
uri = "bolt://localhost:7687"  # Change this to your Neo4j server URL
username = "neo4j"
password = "12345678"

# Define the paths to the CSV files
addresses_file = "file:///test-addresses.csv"
officers_file = "file:///test-officers.csv"
relationships_file = "file:///test-relationships.csv"
example_file = "file:///example.csv"


# Define the Cypher queries for creating nodes and relationships
create_address_query = """
LOAD CSV WITH HEADERS FROM $addresses_file AS row
CREATE (a:Address {node_id: row.node_id, name: row.name, countries: row.countries, country_codes: row.country_codes})
"""

create_officer_query = """
LOAD CSV WITH HEADERS FROM $officers_file AS row
CREATE (o:Officer {node_id: row.node_id, name: row.name, country_codes: row.country_codes})
"""


create_relationship_query = """
LOAD CSV WITH HEADERS FROM $relationships_file AS row
MATCH (start:Officer {node_id: row.node_id_start})
MATCH (end:Address {node_id: row.node_id_end})
CREATE (start)-[:RELATIONSHIP_TYPE {rel_type: row.rel_type, link: row.link, status: row.status, 
                                  start_date: row.start_date, end_date: row.end_date}]->(end)
"""


create_node_query = """
LOAD CSV WITH HEADERS FROM $example_file AS row
CREATE (p:Person {node_id: toInteger(row.node_id), name: row.name, country_codes: row.country_codes})
"""


def create_and_print_node(tx):
    # Create a node with a "Person" label and a "name" property
    result = tx.run("CREATE (p:Person {name: $name}) RETURN p", name="Alice")
    return result.single()[0]

def run_closeness_centrality(tx):
    result = tx.run("""
    CALL algo.closeness.stream(null, null, {direction: "BOTH", writeProperty: "closeness"})
    YIELD nodeId, centrality
    MATCH (node) WHERE id(node) = nodeId
    SET node.closenessCentrality = centrality
    RETURN node, centrality
    """)
    for record in result:
        print(f"Node ID: {record['node'].id}, Closeness Centrality: {record['centrality']}")


def find_people_with_addresses_in_multiple_countries(tx):
    result = tx.run("""
    MATCH (p:Person)-->(a:Address)
    WITH p, collect(distinct a.countries) as countries
    WHERE size(countries) > 1
    RETURN p.name, countries
    """)
    for record in result:
        print(f"Person: {record['p.name']}, Countries: {record['countries']}")



# Create a connection to the Neo4j database
with GraphDatabase.driver(uri, auth=(username, password)) as driver:
    with driver.session() as session:
            
            """
            Custom Algorithms
            """
            # session.write_transaction(find_people_with_addresses_in_multiple_countries)
            
            
            """
            Import test data (only have to import once)
            """
            session.run(create_address_query, addresses_file=addresses_file)
            session.run(create_officer_query, officers_file=officers_file)
            session.run(create_relationship_query, relationships_file=relationships_file)

            """
            Test if database received the command from the python
            """
            #session.run(create_node_query, example_file=example_file)



            """
            Test If the data can be create and the connection is established between the database
            """
            #created_node = session.write_transaction(create_and_print_node)
            # Print the node's properties
            #print(f"Node ID: {created_node.id}")
            #print(f"Node Properties: {created_node}")

            
