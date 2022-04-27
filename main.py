import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth '+self.token}
        file_name = file_path[file_path.rfind('\\')+1:]
        params = {'path': file_name,'overwrite': 'true'}
        response = requests.get(url, headers=headers, params=params)
        print(response.json())
        url2 = response.json()['href']
        resp = requests.put(url2, data = open(file_path, 'rb'))

if __name__ == '__main__':
    path_to_file = 'D:\GitHub\HW_Requests\домашняя работа.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)