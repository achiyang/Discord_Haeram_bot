import requests
from dotenv import load_dotenv
import os

def get_page():
    # POST 요청 보내기
    response = requests.post(url, data=data, allow_redirects=True)

    # 응답 확인
    if response.status_code == 200:
        return response
    else:
        return response.status_code

# POST 요청을 보낼 URL
url = "https://nlms.gwnu.ac.kr/login/index.php"

# load .env
load_dotenv("user.env")

# POST 데이터에 들어갈 user 데이터
userid = os.environ.get("id")
userpw = os.environ.get("password")

# POST 요청 데이터
data = {
    "username": userid,
    "password": userpw
}

