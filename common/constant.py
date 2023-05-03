import os.path


class Constant:

    # 获取工作根目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    # 配置文件目录
    CONF_DIR = os.path.join(BASE_DIR,"conf"+"/")

    # data文件目录
    DATA_DIR = os.path.join(BASE_DIR,"data"+"/")




