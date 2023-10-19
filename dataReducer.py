# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:50:06 2023

@author: GreifOfUs
"""

import pandas as pd

document = pd.read_csv("filename.csv")
print("START")
print(document.columns)

####
"""
reference website:
    https://www.activestate.com/resources/quick-reads/how-to-delete-a-column-row-from-a-dataframe/
"""
###


#remove column named
#document.drop(["rowNames"], axis = 1, inplace=True)

#remove row in in column named
#document.drop([row#], axis=0, inplace=True)
#document.drop(document.index[(document["column name"] == "target")], axis=0, inplace=True)

#remove missing data
#new_document = document.dropna()

#print the cleaned document
document.to_csv("new_filename.csv") #your choice in names
print("COMPLETE")