from interface.regiester import Interface_register
from interface.login import Interface_login
from common.get_result import get_result_one
from common.sendmethod import SendMethod
import unittest,ddt,os
from common.operationexcel import OperationExcel
from faker import Faker
from common.db import DB


BASE_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0] # 获取当前目录--获取项目目录
CONFIG_FILE = os.path.join(BASE_PATH,'data','add_register.xls')  # 将"data"文件夹添加到当前目录
ERROR_FILE = os.path.join(BASE_PATH,'data','register_data.xls')  # 将"data"文件夹添加到当前目录
error_oper = OperationExcel(ERROR_FILE)
test_data= error_oper.get_data_for_dict()


@ddt.ddt
class Test_register(unittest.TestCase):
    def setUp(self) -> None:
        self.oper = OperationExcel(CONFIG_FILE)
        #实例化db
        self.db = DB()
        self.url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signup'
        self.fk = Faker('zh_CN')

    def test_case_01(self):
        """正向数据注册"""
        name = self.fk.user_name() # 姓名
        email = self.fk.email()  # 邮箱
        phone = self.fk.phone_number()  # 手机号
        password = self.fk.password() # 密码
        id = self.fk.pyint()  # 随机整数
        add_list = []
        add_list.extend([name,email,phone,password])
        self.oper.write_excel(add_list)
        data = {"field": [{"id": id, "value": f"{phone}"}],
                "email": f"{email}", "name": f"{name}",
                "password": f"{password}"}
        response = Interface_register.regiester(method='post',url=self.url,data=data)
        self.result = get_result_one(response, 'succeed')
        self.assertEqual(self.result,1)


        sql = f"select count(*) from ecs_users where user_name = '{name}'"
        datas = self.db.find_one(sql)
        num = datas['count(*)']
        self.assertEqual(num,1)



        del_sql = f"delete from ecs_users where user_name='{name}'"
        self.db.execute(del_sql)


    @ddt.data(*test_data)
    def test_case_02(self,data):
        """逆向数据注册"""
        data = {"field": [{"id": 123, "value": f"{data['phone']}"}],
                "email": f"{data['email']}", "name": f"{data['name']}",
                "password": f"{data['password']}"}
        response = Interface_register.regiester(method='post', url=self.url, data=data)
        result = get_result_one(response, 'succeed')
        self.assertEqual(result,0)


        #写一个sql语句
        sql = f"select count(*) from ecs_users where user_name = '{data['name']}'"
        #执行sql
        datas = self.db.find_one(sql)
        num = datas['count(*)']
        self.assertEqual(num,0)

        del_sql = f"delete from ecs_users where user_name='{data['name']}'"
        self.db.execute(del_sql)


if __name__ == '__main__':
    unittest.main()
