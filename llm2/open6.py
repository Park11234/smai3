import urllib

from myllm.Myapi import openAiModel, openAiModelArg, makeMsg


def test(prompt):
    openModel = openAiModel()
    print("")
    response = openModel.images.generate(

        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    print(image_url)
    imgName = "img/dogncat.png"
    urllib.request.urlretrieve(image_url, imgName)

if __name__ == '__main__':
    prompt = "골든 햄스터 사실적으로 그려줘 배경은 대학교 강의실"
    test(prompt)