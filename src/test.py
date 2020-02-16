#!/usr/bin/python
import csv
from elasticsearch import helpers, Elasticsearch
import sys

fileName="EQ_ISINCODE_"+sys.argv[1]+".CSV"
INDEX_NAME="bse"+sys.argv[1]
print fileName
print INDEX_NAME
print sys.argv[2]
#es = Elasticsearch([{'host':'localhost','port':9200}])
#
#with open(fileName) as f:
#    reader = csv.DictReader(f)
#    print type(reader)
#    row['timestamp'] = sys.argv[2]
#    reader.append(row)
#    helpers.bulk(es, reader, index=INDEX_NAME, doc_type='document')
#    for row in reader:
#        value = row['TRADING_DATE']
#        row['temestamp'] = sys.argv[2]
#        es.index(index=INDEX_NAME, doc_type='document',body=row)
#        print row
