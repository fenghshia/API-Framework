'''
执行windows的命令
替换输出里面的\n为  \n
'''
from os import system
from subprocess import Popen, PIPE


class read_cmd:

    # 只返回有无错误
    def system(self, cmd):
        r = system(cmd)
        if r == 0:
            return True
        else:
            return False

    # 返回的运行内容可以被处理
    def sub_popen(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        r = p.communicate()
        return r[0].decode('utf-8')
