
import requests, os, bs4
url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith("#"):
    print("Downloading the page...")
    res = requests.get(url)
    res.raise_for_status()
    try:
        soup = bs4.BeautifulSoup(res.text, 'lxml')
    except bs4.FeatureNotFound: 
        soup = bs4.BeautifulSoup(res.text,'html.parser')
    comic_element = soup.select('#comic img')
    if comic_element == 0:
        print("No comic image found!!..")
    else:
        comic_image_url = comic_element[0].get('src')
        print("Downloading the images..", (comic_image_url))
        res = requests.get('http:' + comic_image_url)
        res.raise_for_status()

        file = open(os.path.join('xkcd',os.path.basename(comic_image_url)),'wb')
        for chunk in res.iter_content(10):
            file.write(chunk)
        file.close()
    prev_link= soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prev_link.get('href')
print("Done")