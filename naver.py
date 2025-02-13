def naver():
    import os
    import sys
    import urllib.request
    from dotenv import load_dotenv
    import json
    
    load_dotenv()
    client_id = os.environ.get("MY_ID")
    client_secret = os.environ.get("MY_SECRET")
    
    encText = urllib.parse.quote("속보")
    url = "https://openapi.naver.com/v1/search/news.json?query=" + encText + '&display=5&start=1&sort=sim'
    # JSON 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = response_body.decode('utf-8')
    data = json.loads(result)
    ldata = data['items']
    for n in ldata:
        print(n['title'].replace('<b>','').replace('<b>',''))
        print(n['description'])
        print(n['originallink'])    
else:
    print("Error Code:" + rescode)