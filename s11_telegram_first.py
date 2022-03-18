import http.client
import json
# https://api.telegram.org/bot5170312845:AAGPm9CouabUbQZy18T4RI2g-8_70xsFi9Y/getUpdates

MY_TOKEN = '5170312845:AAGPm9CouabUbQZy18T4RI2g-8_70xsFi9Y'

# 본인의 채팅 아이디를 입력하시오
myChatId = 1856600570

# 보내고 싶은 메세지를 적어보세요
myText = '컴퓨터야 내 메세지 텔레에 보내봐'

# https://api.telegram.org/bot[봇토큰]/sendmessage?chat_id=[챗아이디]&text=[보낼메시지]
# https://api.telegram.org/bot111111:AAFLkKc_jA8SX9Fnlsgd_w3eFf9g5CBVyPQ/getUpdates

def tele(MY_TOKEN,myChatId,myText):
    TELEGRAM_API_HOST = 'api.telegram.org'
    connection = http.client.HTTPSConnection(TELEGRAM_API_HOST)

    # 토큰과 메서명 지정
    url = f"/bot{MY_TOKEN}/sendMessage"

    # HTTP 헤더
    headers = {'content-type': "application/json"}

    # 파라미터
    param = {
        'chat_id': myChatId,
        'text': myText
    }

    # Http 요청
    connection.request("POST", url, json.dumps(param), headers)

    # 응답
    res = connection.getresponse()

    # Response body 출력
    # print(json.dumps(json.loads(res.read().decode()), indent=4))
    # print('응답코드 : ', res.status)
    # print('메시지 : ', res.msg)

    # 연결 끊기
    connection.close()

if __name__=='__main__':
    tele(MY_TOKEN,myChatId,myText)


