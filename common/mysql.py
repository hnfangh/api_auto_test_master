
import pymysql
from common.configer import Configer
from common.log import Log


class MysqlHelp:


    def __init__(self):
        self.host = Configer.conf_ini("TEST","host","mysql")
        self.port = Configer.conf_ini("TEST","port","mysql")
        self.user = Configer.conf_ini("TEST","user","mysql")
        self.password = Configer.conf_ini("TEST","password","mysql")
        self.db = None
        self.charset = "utf-8"

    # todo 建立连接，创建游标
    def connect(self):
        self.con = pymysql.connect(host=self.host,port=int(self.port),user=self.user,password=self.password,db=self.db,charset=self.db)
        self.cursor = self.con.cursor(pymysql.cursors.DictCursor) # 设置返回数据类型为字典


    # todo 查询单条数据
    def get_one(self, sql):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close_all()
        except Exception as e:
            Log().error("select one error ------>".format(e))
        return result


    # todo 查询多条数据
    def get_all(self, sql):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close_all()
        except Exception as e:
            Log().error("select one error ------>".format(e))
        return result


    # todo 执行SQL新增\删除\修改操作，提交&回滚
    def __exec(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.con.commit()
            self.close_all()
        except Exception as e:
            Log().error("rollback ----->".format(e))
            self.con.rollback()
    # 新增
    def insert(self,sql):
        return self.__exec(sql)

    # 更新
    def update(self,sql):
        return self.__exec(sql)

    # 删除
    def delete(self,sql):
        return self.__exec(sql)

    # todo 关闭连接
    def close_all(self):
        self.cursor.close()
        self.con.close()

if __name__=="__main__":
    sql = "select * from xxx;"
    res = MysqlHelp().get_one(sql)
    print(res["id"])


