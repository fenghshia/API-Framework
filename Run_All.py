'''
主方法运行测试
输出全部写入日志.md
'''
from datetime import datetime
from API_Framework.Util.Cmd import read_cmd


if __name__ == "__main__":

    # 对象
    cmd = read_cmd()

    # 命令
    delCmd = "rd /s /q Report\\html Report\\xml"
    RunTestCmd = "pytest Cases -s -q --alluredir Report/xml"
    ReportCmd = "allure generate Report/xml -o Report/html --clean"

    # 标记参数

    # 记录运行日志
    with open("./Report/日志.md", "a") as f:
        t = datetime.now()
        f.write(f"# {t.year}-{t.month}-{t.day}\n")
        f.write(f"### {t.hour}:{t.minute}:{t.second}运行\n")
        # 删除之前生成的报告
        f.write("删除上次生成的报告  \n")
        cmd.system(delCmd)
        f.write("运行脚本  \n")
        f.write(cmd.sub_popen(RunTestCmd).replace('\n', '  \n'))
        f.write("生成报告  \n")
        f.write(cmd.sub_popen(ReportCmd).replace('\n', '  \n'))
