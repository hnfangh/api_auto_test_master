
import yaml

from common.baseapi import BaseApi
from common.constant import Constant
from common.log import Log
from common.shelvedb import ShelveDB

class Login(BaseApi):

    token_file = "token.db"
    key = "auth"

    # todo 模板替换
    # def template(self):
    #     with open(Constant.CONF_DIR + "token.yaml") as f:
    #         st = string.Template(f.read()).substitute(isPlugin='true')
    #     Log().info("替换后的值=>>>>>{}".format(st))
    #     return yaml.safe_load(st)

    # todo 登录提取token，并存入DB中
    def login(self):
        # 3次重试
        for i in range(3):
            data = yaml.safe_load(open(Constant.CONF_DIR+"token.yaml"))
            res = self.http_api(data)
            if res.json()["code"] == 0:
                Log().info("登录成功，获取到的Token为: {}".format(res.json()["data"]["token"]))
                value = res.json()["data"]["token"]
                # 把token值存入到DB中
                ShelveDB().create_db(self.token_file, self.key, value)
                token = ShelveDB().get_db(self.token_file, self.key)
                return token
            else:
                Log().info(f"登录失败<========{res}")


if __name__=="__main__":
    print(Login().login())

