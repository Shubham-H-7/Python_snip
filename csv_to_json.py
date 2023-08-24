import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as csv_input:
        csv_reader = csv.DictReader(csv_input)
        for row in csv_reader:
            data.append(row)

    with open(json_file, 'w') as json_output:
        json.dump(data, json_output, indent=4)

csv_file_path = '/Users/shubham/Downloads/300_Rec.csv'  # Replace with your CSV file path
json_file_path = '/Users/shubham/Downloads/csv_to_json.json'  # Replace with your desired JSON file path

csv_to_json(csv_file_path, json_file_path)
