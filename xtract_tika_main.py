import json
import tika
import os
import argparse

tika.TikaClientOnly = True
# tika.TIKA_SERVER_JAR="file://tika-tester/tika-server-1.24-bin/tika-server.jar"
from tika import parser

# tika.tika.TikaServerJar = "file://tika-tester/tika-server-1.24-bin/tika-server.jar"
# tika.tika.TikaServerLogFilePath = ""


# print(tika.tika.TikaLogFile)

# Parses a single file
def parse_file(path):
    print(f"Path: {path}")
    print(type(path))
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
# parse_file('coviddata2021-02-13.csv')


def execute_extractor(path):
    get_data = parse_file(path)
    return get_data

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('--path')
    args = ap.parse_args()
    path = args.path

    x = parse_file(path)
    print(f"Metadata: {x}")

