"""
===+++ TXT Bing Image Url +++===
Author : Dagimal
Date : 15-May-2021
E-mail : daffagifariakmal@gmail.com
"""

from bing_image_urls import bing_image_urls
from tqdm import tqdm

imgs_file = 'image_keyword.txt'
imgs = open(imgs_file, 'r').readlines()
number_of_lines = len(imgs)
print(number_of_lines)
print('FILE '+imgs_file+' ADA '+str(number_of_lines)+' BARIS')
print('INDEX AWAL NYA ADALAH 0')
print('=========================\n')
# INPUT
fileName = input('Nama File Output : ')
awal = int(input('Index Awal : '))
akhir = int(input('Index Akhir : '))

pbar = tqdm(total = int(akhir))
while awal <= akhir:
	try:
		f = open(fileName+'.txt', 'a')
		print(''.join(bing_image_urls(imgs[awal], limit=1)), file=f)
		awal += 1
		pbar.update(1)
	except Exception as e:
		print(e)
		#print('https://1.bp.blogspot.com/-Q9ZaBpyBN5k/YI6JfF39ylI/AAAAAAAABj0/AOU6aGdsfAMkmecCKfvrnE1VIv7K11fMgCLcBGAsYHQ/s320/allrecipes.png', file=f)
