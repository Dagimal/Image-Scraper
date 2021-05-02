from jmd_imagescraper.core import * # dont't worry, it's designed to work with import *
from pathlib import Path
from tqdm import tqdm


pbar = tqdm()
#root = Path().cwd()/"images"

#duckduckgo_search(root, "Cats", "sate ayam", max_results=1000)
##duckduckgo_scrape_urls("cat", max_results=1)

#print(links)

#save_urls_to_csv(root, "cats", "ayam goreng", max_results=100)
#duckduckgo_scrape_urls("cats", 100)

resep = open('image_keyword.txt','r').readlines()
#loop = -1
#while loop <= len(resep):
#	loop += 1
#	f = open('hasil.txt','a')
#	links = duckduckgo_scrape_urls(resep[loop], max_results=1)
#	print(links, file=f)
#print(type(links))


params = {
    "max_results": 1,
    "img_size":    ImgSize.Medium, 
    "img_type":    ImgType.Photo,
    "img_layout":  ImgLayout.All,
    "img_color":   ImgColor.Purple
}

loop=1
while loop <= len(resep):
	f = open('gambar.txt','a')
	loop += 1
	links = duckduckgo_scrape_urls(resep[loop], **params)
	print(''.join(links), file=f)

#links = duckduckgo_scrape_urls("happy clowns", max_results=3)
#print(links)
