import requests
from bs4 import BeautifulSoup

# 코로나 요약 현황을 가져오는 함수
def get_corona_summary():
    url = "http://ncov.mohw.go.kr/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    res = requests.get(url,headers=headers)

    soup = BeautifulSoup(res.text,'lxml')
    # print(soup)

    # 확진환자/완치/치료중/사망 수 가져오기
    peoples = soup.select('.liveNumOuter ul.liveNum .num')
    # print(peoples)

    # 데이터 정리
    results=[
        {'key':'확진환자', 'value':int(peoples[0].text.replace(',','').replace('(누적)',''))},
        {'key':'완치', 'value':int(peoples[1].text.replace(',',''))},
        {'key':'치료중', 'value':int(peoples[2].text.replace(',',''))},
        {'key':'사망', 'value':int(peoples[3].text.replace(',',''))}
    ]
    # print(results)
    return results


# 테스트 용 코드
if __name__ == "__main__":
    print(get_corona_summary())