from common.baseapi import BaseApi
from common.log import Log


class DingTalk(BaseApi):


    @classmethod
    def send_dingtalk(self,msg):
        """
        发送钉钉通知消息
        :param msg: 消息体
        :return:
        """

        data = {
            "method": "POST",
            "url" : "https://oapi.dingtalk.com/robot/send",
            "params":{"access_token": "xxxxae6339436663643f03a6fdebxxxx722c798480c1ee1e88xxxx"},
            "headers": {"content-type": "application/json"},
            "json": msg
            }

        res = self.http_api(data)
        if res.json()["errcode"] == 0:
            Log().info("钉钉通知成功<============")
        else:
            Log().info("钉钉通知失败<============")


if __name__ == "__main__":
    ding = DingTalk()
