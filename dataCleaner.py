# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:47:37 2023

@author: James Ellis
"""

import pandas as pd

#slow section
addresses = pd.read_csv("nodes-addresses.csv")
entities = pd.read_csv("nodes-entities.csv")
intermediaries = pd.read_csv("nodes-intermediaries.csv")
officers = pd.read_csv("nodes-officers.csv")
others = pd.read_csv("nodes-others.csv")
relationships = pd.read_csv("relationships.csv")
#slow section


# print(addresses.head())
print(addresses.columns)
print(len(addresses.columns))
#print(entities.head())
print(entities.columns)
print(len(entities.columns))
#print(intermediaries.head())
print(intermediaries.columns)
print(len(intermediaries.columns))
#print(officers.head())
print(officers.columns)
print(len(officers.columns))
#print(others.head())
print(others.columns)
print(len(others.columns))
#print(relationships.head())
print(relationships.columns)
print(len(relationships.columns))

"""
think about what you need to do?
do we want to eliminate certain data points?
"""

#print("\n\ncleaning start\n\n")
print("\n\nremove unwanted columns\n\n")

#data cleanse addresses
addresses.drop(["note", "sourceID", "valid_until", "address"], axis = 1, inplace=True)

#data cleanse entities
entities.drop(["note", "sourceID", "valid_until"], axis = 1, inplace=True)

#data cleanse intermediaries
intermediaries.drop(["note", "address", "sourceID", "valid_until",
                     "internal_id", "country_codes"], axis = 1, inplace=True)

#data cleanse officers
officers.drop(["note", "countries", "sourceID", "valid_until"], axis = 1, inplace=True)
#jurisdiction_description will not be removed

#data cleanse other
others.drop(["note", "sourceID", "valid_until", "jurisdiction_description"], axis = 1, inplace=True)

#data cleanse relationships
relationships.drop(["sourceID"], axis = 1, inplace=True)


#
print("\n\nreduction done\n\n")

#look around
"""
print("\n\n")
temp = addresses.loc[addresses["node_id"] == 120004328]
print(temp.to_string())
print("\n\n")
"""
#done playing
"""
# print(addresses.head())
print(addresses.columns)
print(len(addresses.columns))
#print(entities.head())
print(entities.columns)
print(len(entities.columns))
#print(intermediaries.head())
print(intermediaries.columns)
print(len(intermediaries.columns))
#print(officers.head())
print(officers.columns)
print(len(officers.columns))
#print(others.head())
print(others.columns)
print(len(others.columns))
#print(relationships.head())
print(relationships.columns)
print(len(relationships.columns))
"""

print("\n\nstart removing dirty data\n\n")

"""
you need to itteratively go through and find "error prone data" 
go through each line of data and if missing remove said node from everywhere (especiallly relationships)
go until you reach the end
"""
print("WARNING SLOW DATA PROCESSING")
"""
#name.dropna() #drops rows wehere at least 1 element is missing
missing_addresses = addresses.isnull() #can put into address[] for info
#addresses[missing_addresses].to_csv("missing-addresses.csv", mode = 'w', index = False)
missing_entities = entities.isnull()
#entities[missing_entities].to_csv("missing-entities.csv")
missing_intermediaries = intermediaries.isnull()
#intermediaries[missing_intermediaries].to_csv("missing-intermediaries.csv", mode = 'w', index = False)
missing_officers = officers.isnull()
#officers[missing_officers].to_csv("missing-officers.csv", mode = 'w', index = False)
missing_others = others.isnull()
#others[missing_others].to_csv("missing-others.csv", mode = 'w', index = False)
missing_relationships = relationships.isnull()
#relationships[missing_relationships].to_csv("missing-relationships.csv", mode = 'w', index = False)
"""
print("\nFOUND ALL MISSING DATA\nREMOVING ALL NODES MISSING DATA\n")
#need to find node_id in each and remove said node_id from all

#temp = entities[entities.loc("node_id" = node_id)] #repeat for all others
#go through you missing_x until all of missing x is removed from x,y,z
#if(missing_addresses["node_id"][x] == True)

#remove everything that is missing?
#then go through the relationships remaining and remove all missing links?
clean_addresses = addresses.dropna()
clean_entities = entities.dropna()
clean_intermediaries = intermediaries.dropna()
clean_officers = officers.dropna()
clean_others = others.dropna()
###data cleaned outside of relationships###
print("\nCHECKING RELATIONSHIPS\n")
for x in range(len(relationships)):
    print(x, " out of ", len(relationships))









#### completed cleaning

print("\n\ncleaning done\n\n")


print("begin printing new .csv\n")
clean_addresses.to_csv("reduced-addresses.csv", mode = 'w', index = False)
clean_entities.to_csv("reduced-entities.csv")
clean_intermediaries.to_csv("reduced-intermediaries.csv", mode = 'w', index = False)
clean_officers.to_csv("reduced-officers.csv", mode = 'w', index = False)
clean_others.to_csv("reduced-others.csv", mode = 'w', index = False)
relationships.to_csv("reduced-relationships.csv", mode = 'w', index = False)

print("\n\ndone\n\n")
