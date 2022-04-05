import requests
list_of_heroes = ['Hulk', 'Captain America', 'Thanos']


def the_most_intelligence(names_list):
    dict_of_heroes = {}
    for name in list_of_heroes:
        url = "https://superheroapi.com/api/2619421814940190/search/{}".format(name)
        resp = requests.get(url)
        for el in resp.json()['results']:
            if el['name'] == name:
                dict_of_heroes[name] = int(el['powerstats']['intelligence'])
    print(max(dict_of_heroes))


if __name__ == '__main__':
    the_most_intelligence(list_of_heroes)


file_list = ['test.txt', 'txt.txt', 'cook_book.txt', 'c.docx']


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        for file in file_list:
            headers = {
                'Content-Type': 'application/json',
                'Authorization': '{}'.format(self.token)
            }
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            params = {"path": file, "overwrite": "true"}
            response = requests.get(upload_url, headers=headers, params=params)
            href_json = response.json()
            href = href_json['href']
            response = requests.put(href, data=open(file_path, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print("Success")


if __name__ == '__main__':
    path_to_file = 'C:/Projects/Heroes.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
