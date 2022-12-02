import sys, requests, re

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "deflate",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"TE": "trailers"}

response = requests.get("%s"% sys.argv[1] ,headers)
for links in re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', response.text):
    response2 = requests.get(links, headers)
    if response2.status_code == 200:
        print(links)
    else:
        print('links with 404 found')
