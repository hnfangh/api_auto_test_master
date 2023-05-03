
import shelve
from common.constant import Constant

class ShelveDB:

    # todo 创建db持久化
    def create_db(self,filename,key,value):
        with shelve.open(Constant.CONF_DIR+str(filename)) as db:
            db[key] = value


    # todo 查询key->value
    def get_db(self,filename,key):
        with shelve.open(Constant.CONF_DIR+str(filename),"r") as db:
            # print(db.get(key))
            return db.get(key)



if __name__ == "__main__":
    db = ShelveDB()
    db.create_db("token.db","auth","Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.")
    db.get_db("token.db","auth")