import requests

n = input('당신의 영어이름은? : ')
url = f"https://api.agify.io/?name={n}"

response = requests.get(url).json()

print(f'{n}의 나이는 {response["age"]}살 입니다.')
