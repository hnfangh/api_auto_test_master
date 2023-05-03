import yaml

from common.constant import Constant


class Conver:

    def json2yaml(self,data,filename:str):
        with open(Constant.CONF_DIR+f"{filename}.yaml", "w") as fp:
            yaml.dump(data,fp)



    def yaml2json(self):
        pass



if __name__ == "__main__":

    data = {
        "method": "POST",
        "url": "https://xxx.xxxx.cn/api/login",
        "json": {"password":"xxx","phoneNumber":"xxx","uuid":"xxx-4566-9e10-xxx93-85a5f"},
        "headers": {"content-type": "application/json"}
    }

    conv = Conver()
    conv.json2yaml(data,"token")
