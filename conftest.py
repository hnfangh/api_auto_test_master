# coding=utf-8
import os
import time
from common.log import Log
from common.dingtalk import DingTalk
from common.configer import Configer
import json
from common.constant import Constant

# todo hook执行后调用收集报告结果
def pytest_terminal_summary(terminalreporter):
    """
    收集测试结果
    :param terminalreporter:
    :param exitstatus:
    :param config:
    :return:
    """
    total = terminalreporter._numcollected
    passed = len([i for i in terminalreporter.stats.get("passed",[]) if i.when != "teardown"])
    failed = len([i for i in terminalreporter.stats.get("failed",[]) if i.when != "teardown"])
    error = len([i for i in terminalreporter.stats.get("error",[]) if i.when != "teardown"])
    skipped = len([i for i in terminalreporter.stats.get("skipped",[]) if i.when != "teardown"])
    successful = round(passed / total * 100, 2)
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    # 消息体中具体发送内容
    msg_text = '## **接口自动化测试执行结果**\n\n ' \
               '**项目名称：** api_auto_test\n\n ' \
               '**报告地址：**[点击跳转详情](https://xxx/allure/)\n\n ' \
               '**用例总数量：** <font color="#FFA500">{}</font>\n\n ' \
               '**成功数量：** <font color="#008000">{}</font>\n\n ' \
               '**失败数量：** <font color="#FF0000">{}</font>\n\n ' \
               '**跳过数量：** <font color="#FFD700">{}</font>\n\n ' \
               '**通过率：** <font color="#FFA500">{}%</font>\n\n ' \
               '**相关人员：** @小钉\n\n ' \
               '**执行时间:** {}'.format(total, passed, failed, skipped, successful, now)
    # 通知消息模板
    with open(Constant.CONF_DIR+"msg.json",'r',encoding="utf-8") as file:
        result = json.load(file)
        result["markdown"]["text"] = msg_text   # 重新赋值原来的text内容

    # 打印收集的统计数据
    Log().info("TOTAL:{}  PASSED:{}  FAILED:{} SKIPPED:{} SUCCESSFUL:{}%".format(total,passed,skipped,failed,successful))

    # todo 钉钉群通知开关->conf:notification
    # if Configer.conf_ini("DINGTALK","send_key","notification")=="True":
    # 新增钉钉通知开关设置改为读取docker环境变量值，在jenkins构建时动态控制
    if os.getenv("send_key")==True:
        Log().info("钉钉通知开关状态为：【开启】")
        DingTalk.send_dingtalk(result)
    else:
        Log().info("钉钉通知开关状态为：【关闭】")

