import requests
import os

URL = 'https://random.dog/woof.json'
payload = {'filter' : 'mp4,webm'}
DIRECTORY = 'API/lesson_1/photos'
if not os.path.isdir(DIRECTORY):
    os.mkdir(DIRECTORY)
    
for i in range(10):
    response = requests.get(URL, params = payload)
    pict_link = response.json()['url']
    basename, extension = os.path.splitext(pict_link)
    file_name = f'dog{i + 1}{extension}'
    file_path = os.path.join(DIRECTORY, file_name)
    response = requests.get(pict_link)
    with open(file_path, 'wb') as file:
        file.write(response.content)
