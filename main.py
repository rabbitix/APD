from bs4 import BeautifulSoup
import requests
from time import sleep


def add_to_urls(direct_url):
    with open('urls.txt', 'a') as file:
        file.write(f'{direct_url} \n')


url = input("Paste the url here:> ")
# url = "https://www.aparat.com/playlist/5559136"
playlist_id = url.split('playlist/')[-1]
the_url = f"https://www.aparat.com/api/fa/v1/video/playlist/one/playlist_id/{playlist_id}"
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}
playlist_data = requests.get(the_url, headers=headers).json()


def get_hq_download_link(video: dict, playlist_id):
    video_uid = video['attributes']['uid']
    u = f"https://www.aparat.com/api/fa/v1/video/video/show/videohash/{video_uid}?playlist={playlist_id}&pr=1&mf=1"
    data = requests.get(u,headers=headers).json()
    return data['data']['attributes']['file_link_all'][-1]['urls'][0]

videos = [v for v in playlist_data['included'] if v['type'] == 'Video']

for _,video in enumerate(videos,1):
    download_url = get_hq_download_link(video, playlist_id)
    add_to_urls(download_url)
    print(f"extracted video #{_}")
    sleep(.1)
