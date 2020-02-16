#!/usr/bin/python3

import dask.dataframe as dd
from elasticsearch import helpers, Elasticsearch
import csv
import os

nse_fname='out.csv'
bse_fname='combo.csv'
df1 = dd.read_csv(nse_fname)
df = dd.read_csv(bse_fname)
INDEX_NAME='combineddata'
# to delete use
#curl -X DELETE "localhost:9200/combineddata?pretty"

df.compute()
df1.compute()
test = dd.merge(df, df1,on='ISIN', how='left')
test.compute()

test.to_csv('combo1.csv', single_file= True)
os.system("sed -i '1 s/^,/SEQNUM1,/' combo1.csv")
#os.system("sed -i 's/13-Feb-20/2020-02-13/g' combo.csv")

es = Elasticsearch()

with open('combo.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index=INDEX_NAME, doc_type='document')

