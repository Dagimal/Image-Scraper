# ///////////////////////////////////////////////////
#      Google Image URL Search      
#        Created by Dagimal         
#              v0.1                  
# --- Search & Grab URL From Google Search Engine --- 
# //////////////////////////////////////////////////

# CTRL + Z for kill process

import random
import csv
import os
import itertools
from tqdm import tqdm
from simple_image_download import simple_image_download as simp

# CSV Column
title = 1

# Nilai Random Gambar, semakin besar semakin acak tapi semakin lemot
# randomValue = 1

# Simple Image Download
response = simp.simple_image_download

# Buat File
fileName = input("File Name : ")

# Input Batas
#print("Dimulai dari 1")
awal = input("Batas Awal : ")
akhir = input("Batas Akhir : ")
#akhir = awal + 1000

i, j = int(awal), int(akhir)
pbar = tqdm()
with open('src/dataset/full_dataset.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in tqdm(itertools.islice(readCSV, i, j+1)):
                try:
                        #print("--- CTRL + Z for kill process ---")
		        # Export Data
                        f = open(fileName + ".txt", "a")
                        print(''.join(response().urls(row[title], 1)), file=f)
                except Exception as e:
                        print(e)
