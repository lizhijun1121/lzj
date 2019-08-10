from common.sendmethod import SendMethod
from common.get_result import get_result_one
from interface.login import Interface_login
from faker import Faker

class Interface_register:
    @staticmethod
    def regiester(method,url,data):
        response = SendMethod.send_method(method=method,url=url,data=data)
        return response


if __name__ == '__main__':
    fk = Faker('zh_CN')
    name = fk.user_name()  # 姓名
    email = fk.email()  # 邮箱
    phone = fk.phone_number()  # 手机号
    password = fk.password()  # 密码
    id = fk.pyint()  # 随机整数
    print(fk.ssn())#身份证号
    # 自定义长度的随机字符串
    print(fk.pystr(min_chars=None, max_chars=10))
    print(fk.user_name())
    add_list = []
    add_list.extend([name, email, phone, password, id])
    print(add_list)

    print("地址类".center(20, "-"))
    print(fk.address())  # 海南省成市丰都深圳路p座 425541
    print(fk.street_address())  # 深圳街X座









