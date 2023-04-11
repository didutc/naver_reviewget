import requests
import doubleagent
import json
import pandas as pd
import time
url = 'https://smartstore.naver.com/felizdiosa/products/6233092561?NaPm=ct%3Dlgbu7w3k%7Cci%3D5562b32d120d97490ed0947ff5a5a1158778ad61%7Ctr%3Dslsl%7Csn%3D2910011%7Chk%3D54848e234ecdf8a3d418e29924cee06b85d997c3'
text = requests.get(url).text

mallname = url.split('/')[3]





final_lst = []
merchantNo = doubleagent.pinset(text,'"payReferenceKey":"','"')
originProductNo = doubleagent.pinset(text,'"productNo":"','"')
pagenum = 1
while True:
    datas= {"merchantNo" : str(merchantNo),
            "originProductNo" : str(originProductNo),
            "page" : str(pagenum),
            "pageSize" :  "20",                
            "sortType" :"REVIEW_CREATE_DATE_DESC"
    }


    headers= {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",

        "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",

        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "referer": """https://smartstore.naver.com/felizdiosa/products/6233092561?NaPm=ct%3Dlgbyl4lc%7Cci%3D94b53e747909031a046d7e33e84128a923001825%7Ctr%3Dslsl%7Csn%3D2910011%7Chk%3D90a53e75cb00d0ae85f34e3a980208d25a1b5279""",
        "origin": "https://smartstore.naver.com",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"



    }


    req = requests.post('https://smartstore.naver.com/i/v1/reviews/paged-reviews',headers= headers,data=datas).text

    review = doubleagent.pinset(req,'"reviewContent":"','","')
    if len(review) == 0:
        break

    for li in review:
        li = li.replace('\\n',' ')
        final_lst.append(li)
    pagenum = pagenum + 1
    print(pagenum)
    time.sleep(1)
data = pd.DataFrame({
    '리뷰': final_lst,

})
data.to_csv(mallname+".csv", mode='w',index = False , encoding='utf-8-sig')