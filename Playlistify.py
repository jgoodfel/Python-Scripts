from bs4 import BeautifulSoup
import urllib.request
import spotipy

# scrape songs
url= 'https://wknc.org/playlist.php?style=old'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), 'html.parser')

for playlist in soup.find_all('li', class_="playlist-container-section-item-classic"):
        artist=playlist.find_all('div', class_="playlist-container-section-item-classic-artist")
        song=playlist.find_all('div', class_="playlist-container-section-item-classic-song")
        print(artist[0].text,song[0].text)

#connect to spotify     


#add to playlist






    