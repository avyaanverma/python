import requests
import sys
import json

# https://itunes.apple.com/search?entity=song&limit=1&term=
if len(sys.argv) != 2 :
    sys.exit()
artistName = sys.argv[1]
file = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+artistName)

ff = file.json()
# print(ff)


for res in ff["results"]:
    print(res["trackName"] , res["releaseDate"])






