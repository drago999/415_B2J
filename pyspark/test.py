# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:47:22 2023

@author: GreifOfUs
"""

#import pyspark
#import pandas as pd

#addresses = pd.read_csv('test-addresses.csv')
#officers = pd.read_csv('test-officers.csv')
#relationships = pd.read_csv('test-relationships.csv')
"""
print(addresses.head())
print(officers.head())
print(relationships.head())
"""
#makes a spark session #slow start
from pyspark.sql import SparkSession

#creates a session/database that your data will be stored in
spark = SparkSession.builder.appName('testSession').getOrCreate()

#spark
"""
df_spark = spark.read.csv('test-addresses.csv')
print(df_spark.show())
"""
#reads into the dataframe
df_officers = spark.read.option('header', 'true').csv('test-officers.csv')
#shows 

#df_officers.show() would show ENTIRE thing
print(df_officers.head(2))
print('--------')
df_officers.printSchema()

print('--------')
df_relationships = spark.read.csv('test-relationships.csv', header=True, inferSchema=True)
df_relationships.printSchema()
print(df_relationships.columns)
#schema is similar to pandas
#df_name.select('column name') gives you the entire list under that name
#df_hame.select(['col1','col2']) can add .show() to print it
