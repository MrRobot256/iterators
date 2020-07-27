import requests
import json

URL = 'http://en.wikipedia.org/w/api.php'

def get_countries(file):
    country_list = []
    with open(file) as json_file:
        data = json.load(json_file)
        for item in data:
            country_list.append(item['name']['common'])
    return country_list

def write_file(file, data):
    with open(file, 'a') as destination_file:
        for country_link_pair in data:
            json.dump(country_link_pair, destination_file, ensure_ascii=False)
            destination_file.write('\n')


class Wiki_iterator:
    def __init__(self, start=0, end=len(get_countries('countries.json'))-1):
        self.start = start
        self.current = start - 1
        self.end = end
        self.list = get_countries('countries.json')

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration
        self.link = self.get_link(self.current)
        return {self.list[self.current]: self.link}

    def get_link(self, index):
        self.params = {
            'action': 'opensearch',
            'format': 'json',
            'search': self.list[index]
        }
        response = requests.get(URL, params=self.params).json()
        return response[3][0]



write_file('wikipedia_countries_links.json', Wiki_iterator())