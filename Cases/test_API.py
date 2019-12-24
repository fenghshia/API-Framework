import uuid
import pytest
import allure
from json import dumps
from API_Framework.Util.AES import AES_Generater
from API_Framework.Util.Data import Reader
from API_Framework.Util.Requst import Request
from API_Framework.Util.Response import response_judge


# 读取数据对象
aes = AES_Generater()
judge = response_judge()
reader = Reader()
request = Request(aes)


# 通用测试方法
def mod(data):
    # 写入报告的运行步骤
    with allure.step("参数"):
        allure.attach(dumps(data['url'], ensure_ascii=False), "地址")
        allure.attach(dumps(data['data'], ensure_ascii=False), "接口数据")
        allure.attach(dumps(data['result'], ensure_ascii=False), "期望结果包含")
    r = request.send_request(data)
    assert r is not False
    with allure.step("返回值"):
        allure.attach(r)
    assert judge.response_anssert(r['data'], data['result']) is not False


# 路径
path01 = "Json/相亲相关/开启房间/"
title01 = reader.title(path01)
# 脚本测试
@allure.feature(title01["feature"])
@allure.description(title01["description"])
@allure.story(title01["story"])
@pytest.mark.parametrize("data", reader.read(path01))
def test_01(data):
    # 添加uuid
    data['data']['rid'] = "%s" % uuid.uuid1()
    mod(data)
