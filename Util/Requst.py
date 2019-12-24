'''
发送请求
'''
import json
import allure
from requests import session


class Request:

    def __init__(self, aes):
        # 接口地址
        self.http_addr = "http://192.168.2.125:8080/"
        # self.http_addr = "http://192.168.2.310:8080/"
        # 接口进程
        self.Session = session()
        # 加密
        self.aes = aes

    @allure.step("发送请求")
    def send_request(self, data):
        r = self.Session.post(self.http_addr + data['url'],
                              data=self.aes.AES_Encode(json.dumps(data["data"],
                                                                  ensure_ascii=False)))
        if r.status_code == 200:
            try:
                return json.loads(self.aes.AES_Decode(r.text))
            except Exception:
                return json.loads(r.text)
        else:
            allure.attach(r.status_code, "状态码断言失败")
            return False