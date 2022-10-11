from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import random

def responce_maker(name_song):
    song = name_song.replace(' ', '+')
    user = UserAgent().random
    headers = {'User-Agent': user}
    params = {'song': song}
    url = f'https://eemusic.ru/'
    return requests.get(url, headers=headers, params=params)

def download_track(song):
    responce = responce_maker(song)
    soup = BeautifulSoup(responce.text, "lxml")
    track = soup.find_all("div", class_="chkd")[:3]
    track = random.choice(track)
    get_link = 'https://eemusic.ru' + track.find('a', class_='link').get('href')
    responce_for_download = requests.get(get_link, stream=True)
    name = track.find('span', class_='title').text.strip()
    music = open('/Users/misha/Desktop/music/' + name + '.mp3', 'wb')
    for x in responce_for_download.iter_content(1024 * 1024):
        music.write(x)
    music.close()
    return name
