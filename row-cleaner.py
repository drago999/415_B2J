import pandas as pd
from tqdm import tqdm

# Get distinct types from the reduced-relationshipsl.csv it will return both rel_types and links.
def GetDistinctTypes(file_path):
    # Read the CSV file into a DataFrame
    relationships_df = pd.read_csv(file_path)

    # Get the distinct values in the 'rel_type' and 'link' columns
    distinct_rel_types = relationships_df['rel_type'].unique().tolist()
    distinct_links = relationships_df['link'].unique().tolist()

    return distinct_rel_types, distinct_links


def CleanRelationshipsCSV():
    # Load data from 'reduced-relationships.csv' into a DataFrame 
    reduced_relationships_df = pd.read_csv('original-data/reduced-relationships.csv')

    # Load the rest of 5 csv files
    reduced_addresses_df = pd.read_csv('original-data/reduced-addresses.csv')
    reduced_entities_df = pd.read_csv('original-data/reduced-entities.csv')
    reduced_intermediaries_df = pd.read_csv('original-data/reduced-intermediaries.csv')
    reduced_officers_df = pd.read_csv('original-data/reduced-officers.csv')
    reduced_others_df = pd.read_csv('original-data/reduced-others.csv')

    # Extract unique node_ids from other CSV files
    unique_node_ids = set()
    # Extract unique node_ids from 'reduced-addresses.csv'
    unique_node_ids.update(reduced_addresses_df['node_id'].unique())

    # Extract unique node_ids from 'reduced-entities.csv'
    unique_node_ids.update(reduced_entities_df['node_id'].unique())

    # Extract unique node_ids from 'reduced-intermediaries.csv'
    unique_node_ids.update(reduced_intermediaries_df['node_id'].unique())

    # Extract unique node_ids from 'reduced-officers.csv'
    unique_node_ids.update(reduced_officers_df['node_id'].unique())

    # Extract unique node_ids from 'reduced-others.csv'
    unique_node_ids.update(reduced_others_df['node_id'].unique())

    # Create a list to store missing node_ids
    missing_node_ids = []

    # Iterate Through reduced-relationships.csv
    cleaned_data = []

    with tqdm(total=len(reduced_relationships_df)) as pbar:
        for index, row in reduced_relationships_df.iterrows():
            node_id_start = row['node_id_start']
            node_id_end = row['node_id_end']

        # Check if both node_id_start and node_id_end exist in other CSV files
            if node_id_start in unique_node_ids and node_id_end in unique_node_ids:
                cleaned_data.append(row)
            else:
                missing_node_ids.append(node_id_start)
                missing_node_ids.append(node_id_end)
            pbar.update(1)  # Update progress bar


    # Update and Save Clean Data
    cleaned_relationships_df = pd.DataFrame(cleaned_data)
    cleaned_relationships_df.to_csv('output-data/cleaned-relationships.csv', index=False)

    # Print Missing Node IDs
    with open('output-data/missing_node_ids.txt', 'w') as missing_ids_file:
        for missing_id in missing_node_ids:
            missing_ids_file.write(str(missing_id) + '\n')

    print("Data cleansing and reduction completed.")


# Remove extra node that is not exist in the cleaned-relationships.csv
def Clean5CSV():

    # Load the cleaned relationships data
    cleaned_relationships_df = pd.read_csv('output-data/cleaned-relationships.csv')

    # Extract unique node_id values from both node_id_start and node_id_end
    unique_node_ids = set(cleaned_relationships_df['node_id_start']).union(set(cleaned_relationships_df['node_id_end']))

    # List of the other five CSV file paths
    other_csv_files = [
        'original-data/reduced-addresses.csv',
        'original-data/reduced-entities.csv',
        'original-data/reduced-intermediaries.csv',
        'original-data/reduced-officers.csv',
        'original-data/reduced-others.csv'
    ]

    # Initialize the log file
    log_filename = 'output-data/deleted_nodes_log.txt'
    with open(log_filename, 'w') as log:
        log.write("Deleted Node Log:\n\n")

    # Clean the other five CSV files
    for input_file in other_csv_files:
        output_file = 'output-data/cleaned-' + input_file.split('/')[-1]
        CleanCSV(input_file, output_file, log_filename, unique_node_ids)
    print("Cleaning of other CSV files completed.")

    

def CleanCSV(input_file, output_file, log_file, unique_node_ids):
    # Load data from the input CSV file into a DataFrame
    other_df = pd.read_csv(input_file, )

    # Create a list to store cleaned data
    cleaned_data = []

    # Create a list to store deleted node information
    deleted_nodes = []

    with tqdm(total=len(other_df)) as pbar:
        for index, row in other_df.iterrows():
            node_id = row['node_id']
            if node_id in unique_node_ids:
                cleaned_data.append(row)
            else:
                deleted_nodes.append((node_id, input_file.split('/')[-1]))  # Record deleted node and source file
            pbar.update(1)

    # Save the cleaned data to the output CSV file
    cleaned_data_df = pd.DataFrame(cleaned_data)
    cleaned_data_df.to_csv(output_file, index=False)

    # Log deleted nodes
    with open(log_file, 'a') as log:
        log.write(f"Deleted nodes from {input_file.split('/')[-1]}:\n")
        for node, source_file in deleted_nodes:
            log.write(f"Node: {node} - Deleted from: {source_file}\n")
        log.write("\n")


def clean_csv_with_escape_characters(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Define a function to clean escape characters within double-quoted fields
    def clean_escape_characters(text):
        if isinstance(text, str) and text.count('"') % 2 == 1:
            # If it's a string and there's an odd number of double quotes, remove escape characters
            text = text.replace("\\", "")

            # Remove trailing backslashes in the string
            text = text.rstrip("\\")
            return text
        else:
            return text

    # Apply the cleaning function to the entire DataFrame with a progress bar
    for column in tqdm(df.columns, desc="Cleaning CSV"):
        df[column] = df[column].apply(clean_escape_characters)

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print("CSV data cleaned and saved to", output_file)


def main():

    print("Main")

    clean_csv_with_escape_characters("output-data/cleaned-addresses.csv","output-data/cleaned-addresses01.csv" )

    # Clean5CSV()

    # Call the function to get distinct types
    # distinct_rel_types, distinct_links = GetDistinctTypes('original-data/reduced-relationships.csv')

    # Print or use the lists as needed
    # print("Distinct rel_types:", distinct_rel_types)
    # print("Distinct links:", distinct_links)

    # Call the function to clean and reduce data
    # CleanRelationshipsCSV()
    

if __name__ == "__main__":
    main()