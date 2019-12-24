'''
数据断言
类型和值都会比较
列表为全比较
字典只比较存在的键
'''
import allure
from json import dumps


class response_judge:

    @allure.step("断言")
    def response_anssert(self, r_data, result, sp):
        self.assert_str = True
        if type(r_data) == type(result):
            self.__read(r_data, result, sp)
            return self.assert_str
        else:
            self.__set_false(r_data, result, "返回值与期望值数据类型不相同")
            return self.assert_str

    def __read(self, r_data, result, sp):
        # 判断期望是列表或者元祖,且不为空
        if isinstance(result, (list, tuple)) and result:
            # 判断返回值不为空
            if r_data:
                # 取出两个值
                for i, j in zip(r_data, result):
                    # 判断数据相同
                    if type(i) == type(j):
                        # 自迭代
                        self.__read(i, j, sp)
                    else:
                        self.__set_false(i, j, "结果值与期望值数据类型不同")
            else:
                self.__set_false(r_data, result, "结果值为空,与期望不符")
        # 判断期望是字典,且不为空
        elif isinstance(result, dict) and result:
            # 判断返回值不为空
            if r_data:
                # 取出键
                for k in result.keys():
                    # 判断键在返回值里面
                    if k in r_data:
                        # 判断数据类型相同
                        if type(r_data[k]) == type(result[k]):
                            # 自迭代
                            self.__read(r_data[k], result[k], sp)
                        else:
                            self.__set_false(r_data[k], result[k], "结果值与期望值数据类型不同")
                    else:
                        allure.attach(k, "返回值中不包含此键")
                        self.assert_str = False
            else:
                self.__set_false(r_data, result, "结果值为空,与期望不符")
        # 判断空和内容不同
        elif sp and result != r_data:
            self.__set_false(r_data, result, "数据不相同")
        # 不判断空,只判断内容不同
        elif result != r_data and result and r_data:
            self.__set_false(r_data, result, "数据不相同")

    # 设置错误
    def __set_false(self, r_data, result, name):
        allure.attach(f"期望值:{dumps(result, ensure_ascii=False)}\n结果值:{dumps(r_data, ensure_ascii=False)}",
                      name)
        self.assert_str = False
