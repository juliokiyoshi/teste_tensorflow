import urllib.request
import requests
import sys
import os
from PIL import Image

file = open(sys.argv[1], "r")
i = 0
j = 0
for line in file:
    if (line[-2] == "g"):
        try:
            request = requests.get(line, timeout=0.5, stream=True)
            urllib.request.urlretrieve(line, str(j) + ".jpg")
            try:
                img = Image.open(str(j) + ".jpg")
                img.close()
                print(j)
                j += 1
            except:
                os.remove(str(j) + ".jpg")
                print("Error in line: " + str(i))
        except:
            print("Error in line: " + str(i))
        i += 1
file.close()
