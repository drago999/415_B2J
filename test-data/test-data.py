# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 19:12 2023

@author: Jacob Lin
"""

import pandas as pd
from tqdm import tqdm

def getTestData():
    # Define the input and output file paths
    input_folder = "input/"
    output_folder = "output/"
    addresses_file = "addresses.csv"
    relationships_file = "relationships.csv"
    officers_file = "officers.csv"

    address_df = pd.read_csv(input_folder + addresses_file).head(10)
    address_df.to_csv(output_folder + "test-addresses.csv", index=False)
    node_id_list = address_df['node_id'].tolist()


    relationships_df = pd.read_csv(input_folder + relationships_file)

    filtered_relationships_df = relationships_df[relationships_df['node_id_end'].isin(node_id_list)]
    filtered_relationships_df.to_csv(output_folder + "test-relationships.csv", index=False)
    node_id_start_list = filtered_relationships_df['node_id_start'].tolist()


    officers_df = pd.read_csv(input_folder + officers_file)
    filtered_officers_df = officers_df[officers_df['node_id'].isin(node_id_start_list)]
    filtered_officers_df.to_csv(output_folder + "test-officers.csv", index=False)

    print("Data extraction and export completed.")

def main():
    getTestData()

if __name__ == "__main__":
    main()