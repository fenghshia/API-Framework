'''
读取数据的类
'''
from os import listdir
from json import load


class Reader:

    def read(self, path):
        file_list = listdir(path)
        Json_list = []
        for file_name in file_list:
            if file_name.lower() != "description.json":
                with open(path+file_name, "r", encoding="utf-8") as f:
                    Json_list.append(load(f))
        return Json_list

    def title(self, path):
        with open(path+"Description.json", 'r', encoding='utf-8') as f:
            description = load(f)
        return description
