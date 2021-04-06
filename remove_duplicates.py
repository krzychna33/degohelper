import os
from os.path import isfile, join
from PIL import Image
import imagehash

mypath = "C:\\Users\krzyc\Documents\degoczas"
fnames = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]
hashes = {}
duplicates = []
hash_size=8

for image in fnames:
    with Image.open(os.path.join(mypath, image)) as img:
        temp_hash = imagehash.average_hash(img, hash_size)
        if temp_hash in hashes:
            print("Duplicate {} \nfound for Image {}!\n".format(image, hashes[temp_hash]))
            duplicates.append(image)
        else:
            hashes[temp_hash] = image

counter = 0
if len(duplicates) != 0:
    for duplicate in duplicates:
        os.remove(os.path.join(mypath, duplicate))
        counter+=1

print("Removed {} images".format(counter))