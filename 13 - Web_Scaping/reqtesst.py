import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))

#badRes = requests.get('https://automatetheboringstuff.com/files/dsadas')
# badRes.raise_for_status()

playFile = open('13 - Web_Scaping\\RomeoAndJuliet.txt',
                'wb')  # Binary code for keep the unicode
for chunk in res.iter_content(100000):
    playFile.write(chunk)
