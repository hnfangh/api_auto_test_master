import configparser
import yaml
from common.constant import Constant

class Configer:

    @classmethod
    def conf_ini(self, section, key, file):
        """
        读取ini的配置文件
        :param section:
        :param key:
        :param file: 文件名
        :return:
        """
        config = configparser.RawConfigParser()
        config.read(Constant.CONF_DIR + f'{file}.ini')
        return config.get(section, key)


    @classmethod
    def conf_yaml(self,file):
        """
        读取yaml配置文件
        :param file: 文件名
        :return:
        """
        return yaml.safe_load(open(Constant.CONF_DIR+f"{file}.yaml"))


    @classmethod
    def conf_redis(self):
        pass


if __name__ == "__main__":
    conf = Configer()
    print(conf.conf_ini("TEST", "password","mysql"))
