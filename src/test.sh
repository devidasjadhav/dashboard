#!/bin/bash
#not taking care of holiday as of now.
date2=$(date --date="2020-02-13" +%d%b%Y)
date1=$(date --date="2020-02-13" +%F)
date=$(date --date="2020-02-13" +%d%m%y)
#date=130220
nse_filename='cm'
echo $date $date1
wget https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_$date.zip
unzip EQ_ISINCODE_$date.zip
unzip cm${date2^^}bhav.csv.zip
sed -i '1 s/,/_BSE,/g' EQ_ISINCODE_$date.CSV
sed -i '1 s/ISIN_CODE_BSE/ISIN/' EQ_ISINCODE_$date.CSV

./combine.py $date $date1 ${date2^^}
awk -F, '{print $16}' combo.csv > isin/isin_num
cd isin
scrapy crawl isinget -t csv -o ../out.csv -a isinum=$(readlink -f isin_num)
cd ..
sed -i 's/^ ISIN //' out.csv

./combine1.py

