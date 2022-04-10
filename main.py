import os
import urllib3
from bs4 import BeautifulSoup

source = "https://wallpaperaccess.com/1920x1080-hd-space"
http = urllib3.PoolManager()


def download_wallpapers(url):
    """
        This function will recursively and multi-threaded (tbd) download all images
        from specific url from www.wallpaperaccess.com
        Wallpapers will be saved in new folder in directory  where script will be executed
    """
    url_list = parse_wallpapers(url)
    counter = 1
    print(f"Count {len(url_list)} wallpapers on this page.")
    dir_creator()
    for url in url_list:
        down_url = http.request('GET', url)
        with open(f'Wallpaper_{counter}.jpg', 'wb') as handler:
            print(f'{url} saved as Wallpaper_{counter}.jpg')
            handler.write(down_url.data)
        counter += 1

def dir_creator():
    """ Creates new dir where wallpapers will be downloaded"""
    new_dir = source[28:]
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print(f"Successfully created new dir: {new_dir}")
        print(f"Trying to download wallpapers in {os.getcwd()}")
    else:
        print(f"Dir {new_dir}: already exists, download wallpapers in it anyway?")
        print("All files with same names will be overwritten during this operation")
        answer = input('y/n:   ')
        if answer.lower() == 'y':
            os.chdir(new_dir)
            print(f"Trying to download wallpapers in {os.getcwd()}")
        if answer.lower() == 'n':
            custom_dir = input(f"Enter your custom name for the new dir:   ")
            os.makedirs(custom_dir)
            os.chdir(custom_dir)
            print(f"Successfully created new dir: {custom_dir}")
            print(f"Trying to download wallpapers in {os.getcwd()}")
    return

def parse_wallpapers(url_to_parse):
    """This function parse all images from the passed url and returns list of urls for download"""
    r = http.request('GET', url_to_parse)
    soup = BeautifulSoup(r.data, 'html.parser')
    lst_wp = []
    imgs = soup.findAll('div', attrs={'class': 'wrapper'})
    for img in imgs:
        lst_wp.append("https://wallpaperaccess.com" + img.a['href'])
    return lst_wp


if __name__ == '__main__':
    download_wallpapers(source)
