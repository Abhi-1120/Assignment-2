# importing the requests library
import requests
import json
import csv

# api-endpoint
url = 'https://api.github.com/search/repositories?q=is:public+language:Python+forks:>=200'

# sending get request and saving the response as response object
response = requests.get(url).json()

# fetching all data to data.json file
with open('data.json', 'w') as file:
    json.dump(response, file)

# read all data from data.json file
with open('data.json', 'r') as file:
    data = json.load(file)

# taking csv files as variables
output_csv = "output.csv"
stargazers_count = "stargazers_count.csv"


# Creating methods for writing the data to csv file
def csv_output():
    with open(output_csv, 'w', encoding="utf-8") as file:
        csv_file = csv.writer(file)
        header = csv_file.writerow(
            ['language'.upper(), 'description'.upper(), 'html_url'.upper(), 'watchers_count'.upper(),
             'stargazers_count'.upper(), 'forks_count'.upper()])

        for item in data['items']:
            csv_file.writerow(
                [item['language'], item['description'], item['html_url'], item['watchers_count'],
                 item['stargazers_count'],
                 item['forks_count']])


# Creating methods for writing limited data to csv file
def stargazers():
    with open(stargazers_count, 'w', encoding="utf-8") as file:
        stargazers_file = csv.writer(file)
        stargazers_file.writerow(
            ['language'.upper(), 'description'.upper(), 'html_url'.upper(), 'watchers_count'.upper(),
             'stargazers_count'.upper(), 'forks_count'.upper()])
        for item in data['items']:
            if item['stargazers_count'] > 2000:
                # Code here will only run if the condition is successful
                stargazers_file.writerow(
                    [item['language'], item['description'], item['html_url'], item['watchers_count'],
                     item['stargazers_count'], item['forks_count']])


csv_output()  # function calling
stargazers()  # function calling
