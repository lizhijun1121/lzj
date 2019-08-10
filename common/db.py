#导入模块
import pymysql
#创建类
class DB(object):
    #创建初始化方法   绑定属性
    def __init__(self,host='ecshop.itsoso.cn',user='ecshop',password='ecshop',database='ecshop',charset='utf8'):

        #创建连接 对象
        self.cnn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset)
        #创建游标对象
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.SSDictCursor)

    #创建del魔术方法    在对象被销毁时   关闭游标和连接对象
    def __del__(self):
        #关闭游标
        self.cursor.close()
        self.cnn.close()


#创建一个查找所有的方法
    def find_all(self,sql,arges=None):
        #执行sql
        self.cursor.execute(sql,arges)
        myresult = self.cursor.fetchall()
        return myresult
    def find_one(self,sql,arges=None):
        #查找一个
        self.cursor.execute(sql,arges)
        myresult = self.cursor.fetchone()
        return myresult

    def execute(self,sql,arges=None):
        #写操作
        try:
            # 开启事务
            self.cnn.begin()

            # 通过游标发送sql语句
            num = self.cursor.execute(sql,arges)
            if num > 0:
                # 提交事务
                self.cnn.commit()
                return True
            else:
                # 回滚事务
                self.cnn.rollback()
                return False
        # 如果有异常就进行处理
        except Exception as e:
            # 回滚事务 并打印错误信息
            self.cnn.rollback()
            print(f"代码有误{e}")



if __name__ == '__main__':


    #查找所有
    # db.find_all()

    # #修改
    # sql = "update tb_news set title=%s  where id=%s"
    # args=["李克强",1001]
    # infos=db.execute(sql,args)
    # if infos:
    #     print("更新成功")
    # else:
    #     print("更新失败")

    # #查找所有
    # sql="select * from tb_news"
    # infos=db.find_all(sql)
    # for info in infos:
    #     print(info)

    #查找一个
    # sql="select * from tb_news where id=%s"
    # args=[1003]
    # infos=db.find_all(sql,args)
    # print(infos)
    #实例化DB类
    db = DB()
    #写一个sql语句
    sql = "select count(*) from ecs_users where user_name = 'eassaassacshop'"
    datas = db.find_one(sql)
    data =datas['count(*)']
    print(data)


