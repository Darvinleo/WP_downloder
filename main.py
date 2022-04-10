import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()


def download_wallpapers(url):
    """This will recursively multithreaded (tbd) downloads all images from specific url from wallpaperaccess."""
    url_list = parse_wallpapers(url)
    counter = 1
    for url in url_list:
        down_url = http.request('GET', url)
        with open(f'wallpaper_{counter}.jpg', 'wb') as handler:
            handler.write(down_url.data)
        counter += 1


def parse_wallpapers(url_to_parse):
    """This function parse all images from the passed url and returns list of urls for download"""
    r = http.request('GET', url_to_parse)
    soup = BeautifulSoup(r.data, 'html.parser')
    # print(soup)
    lst_wp = []
    imgs = soup.findAll('div', attrs={'class': 'wrapper'})
    for img in imgs:
        lst_wp.append("https://wallpaperaccess.com" + img.a['href'])
    return lst_wp


if __name__ == '__main__':
    download_wallpapers("https://wallpaperaccess.com/1920x1080-hd-space")
