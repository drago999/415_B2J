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

print("\n\ncleaning start\n\n")

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
print("\n\n")
temp = addresses.loc[addresses["node_id"] == 120004328]
print(addresses.loc[addresses["node_id"] == 120004328])
print("\n\n")

#done playing

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

print("\n\ncleaning done\n\n")

print("begin printing new .csv\n")
addresses.to_csv("reduced-addresses.csv")
entities.to_csv("reduced-entities.csv")
intermediaries.to_csv("reduced-intermediaries.csv")
officers.to_csv("reduced-officers.csv")
others.to_csv("reduced-others.csv")
relationships.to_csv("reduced-relationships.csv")

print("\n\ndone\n\n")
