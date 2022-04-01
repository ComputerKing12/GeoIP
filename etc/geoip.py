import requests
import json

r = requests.get('https://geoip.kde.org/v1/calamares')

data = json.loads(r.content)
data_list = list(data.values())
data_str = str(data_list)
data_chopped = data_str.replace("[", "").replace("]", "").replace("'", "")

print(data_chopped)
