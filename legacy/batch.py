# Goes through all the files in rootdir and saves the metadata to JSON
def save_output(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for filename in files:
            filepath = subdir + os.sep + filename
            output = parse_file(filepath)
            with open(f'output/{filename}.json', 'w') as f:
                json.dump(output, f)