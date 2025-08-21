from io import BytesIO

import requests
from PIL import Image

from myllm.Myapi import geminiModel

def test(prompt, img):
    model = geminiModel()
    response = model.generate_content([prompt, img])
    print(response.text)

if __name__ == '__main__':
    image_url = "https://search.pstatic.net/sunny/?src=http%3A%2F%2Ffile3.instiz.net%2Fdata%2Ffile3%2F2019%2F06%2F16%2F5%2F1%2Fc%2F51c5690281cc0164e0e044cc22968c4e.jpg&type=sc960_832"
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt="이미지에 있는 음료의 영양성분과 칼로리 당함유 양을 알려줘 한글로"
    test(prompt, img)