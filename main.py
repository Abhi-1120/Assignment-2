# importing libraries
import os
import requests
import csv


def get_date():
    # api_endpoint
    url = 'https://api.github.com/search/repositories?q=is:public+language:Python+forks:>=200'
    # sending get request and saving the response as data object
    response = requests.get(url).json()
    return response


def parse_data(data):
    # Initializing list for csv file
    normal_list = []
    stargazers_list = []

    # Loop for appending data using filter for both csv file
    for item in data['items']:
        csv_data = [item['language'], item['description'], item['html_url'], item['watchers_count'],
                    item['stargazers_count'], item['forks_count']]
        normal_list.append(csv_data)

        if item['stargazers_count'] > 2000:
            stargazers_list.append(csv_data)
    return normal_list, stargazers_list


def write_data_to_csv_file(normal_list, stargazers_list):
    # header of the csv file
    header = ['LANGUAGES', 'DESCRIPTION', 'HTML_URL', 'WATCHERS_COUNT', 'STARGAZERS_COUNT', 'FORKS_COUNT']

    # taking csv files as variables
    normal_csv = "normal_csv"
    stargazers_csv = "stargazers_csv"

    if os.path.exists(normal_csv):
        write_csv(normal_csv, normal_list, 'a')
        write_csv(stargazers_csv, stargazers_list, 'a')
    else:
        normal_list.insert(0, header)
        stargazers_list.insert(0, header)

        write_csv(normal_csv, normal_list)
        write_csv(stargazers_csv, stargazers_list)


# write csv file
def write_csv(filename, csv_list, action='w'):
    with open(filename, action, newline="", encoding="utf-8") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(csv_list)


# Calling Methods
data = get_date()
normal_list, stargazers_list = parse_data(data)
write_data_to_csv_file(normal_list, stargazers_list)
