import json
import tika
import os

tika.TikaClientOnly = True
tika.TIKA_SERVER_JAR="file:////tika-server.jar"
from tika import parser

# Parses a single file
def parse_file(path):
    parsed = parser.from_file(path)
    return parsed["metadata"]

# Goes through all the files in rootdir and saves the metadata to JSON
def save_output(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for filename in files:
            filepath = subdir + os.sep + filename
            output = parse_file(filepath)
            with open(f'output/{filename}.json', 'w') as f:
                json.dump(output, f)  
parse_file('coviddata2021-02-13.csv')


