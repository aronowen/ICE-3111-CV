#!/usr/bin/env bash

CSV_FILE=network.csv
GRAPH_JSON=network.json

rm -f $GRAPH_JSON
./csv2json.py $CSV_FILE > temp.json
sed 's/\\//' temp.json > $GRAPH_JSON
rm -f temp.json

python3 -m http.server
