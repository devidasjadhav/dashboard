#!/usr/bin/python3

import dask.dataframe as dd
from elasticsearch import helpers, Elasticsearch
import csv
import os
import sys

print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
nse_fname='cm'+sys.argv[3]+'bhav.csv'
bse_fname='EQ_ISINCODE_'+sys.argv[1]+'.CSV'
df1 = dd.read_csv(nse_fname)
df = dd.read_csv(bse_fname)
INDEX_NAME='combineddata'
# to delete use
#curl -X DELETE "localhost:9200/combineddata?pretty"

df.compute()
df1.compute()
test = dd.merge(df, df1,on='ISIN', how='left')
test.compute()

test.to_csv('combo.csv', single_file= True)
os.system("sed -i '1 s/^,/SEQNUM,/' combo.csv")
os.system("sed -i 's/13-Feb-20/2020-02-13/g' combo.csv")

#es = Elasticsearch()
#
#with open('combo.csv') as f:
#    reader = csv.DictReader(f)
#    helpers.bulk(es, reader, index=INDEX_NAME, doc_type='document')
#
