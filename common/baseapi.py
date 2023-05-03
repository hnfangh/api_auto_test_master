import requests


class BaseApi:


    @classmethod
    def http_api(self,data):
        """
        HTTP(S)请求
        :param data: json-> method,url,data,headers,cookies,params
        :return: json格式数据
        """
        res = requests.request(**data)
        return res

