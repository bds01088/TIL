import random

numbers = list(range(1, 46))
#print(numbers)
#print(random.sample(numbers))
import requests
#requests 사용해서 로또 api에 데이터 요청하고 응답 받은 문서를 출력

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997"
#조회 요청/ 데이터 형태가 json이므로 json() 붙여야함
#200을 피드백으로 받으면 형태가 달라서 뜨는 에러넘버인듯
response = requests.get(url).json()

#print(response)
winners = []
for i in range(1,7) :
    winners.append(response[f'drwtNo{i}'])
print(winners)

for i in range(1000000) :
    lotto = random.sample(numbers, 6)
    count = 0
    for num in lotto :
        if num in winners :
            count = count+1
    if count == 6 :
        print(f'{i}회차 1등')
    
 