from API_Framework.Util.Response import response_judge
import json


def test_response():
    r = response_judge()
    data1 = {
        "token": "b0969ffc143f498bbcb4cf224c68e562",
        "anchor": {
          "id": "vip001",
          "nickname": "风諾",
          "gender": "MALE",
          "age": 18,
          "avatar": "http://image.1qiyue.cc/user/default/3.jpg?x-oss-process=style/webp80",
          "area": "成都"
        },
        "chatUser": [
          {
          # "id": "vip001",
          # "nickname": "风諾",
          # "gender": "MALE",
          # "age": 18,
          # "avatar": "http://image.1qiyue.cc/user/default/3.jpg?x-oss-process=style/webp80",
          # "area": "成都"
          }
        ]
      }

    data2 = {
        "token": "b0969ffc143f498bbcb4cf224c68e562",
        "anchor": {
          "id": "vip001",
          "nickname": "风諾",
          "gender": "MALE",
          "age": 18,
          "avatar": "http://image.1qiyue.cc/user/default/3.jpg?x-oss-process=style/webp80",
          "area": "成都"
        },
        "chatUser": [
          {
          "id": "vip001",
          "nickname": "风諾",
          "gender": "MALE",
          "age": 18,
          "avatar": "http://image.1qiyue.cc/user/default/3.jpg?x-oss-process=style/webp80",
          "area": "成都"
          }
        ]
      }
    r.response_anssert(data2, data1, False)