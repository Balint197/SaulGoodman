from bs4 import BeautifulSoup
import requests

def remove_tags(soupdata):
 
    for data in soupdata(['style', 'script']):
        # Remove tags
        data.decompose()
 
    # return data by retrieving the tag content
    return ' '.join(soupdata.stripped_strings)

with open("cimek.txt") as file:
    lines = [line.rstrip() for line in file]

for url in lines:
    #url='https://njt.hu/jogszabaly/2004-2-20-SY'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

    r=requests.get(url, headers=headers)
    soup1 = BeautifulSoup(r.content, 'html.parser')

    kell = soup1.find_all(id='jogszab')

    fpre = res=url.rsplit('/',1)
    fname = fpre[1]

    with open(fname + '.txt', 'w', encoding='utf-8') as f:
        for x in kell:
            f.write(str(remove_tags(x)))




