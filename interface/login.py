from common.sendmethod import SendMethod
from common.get_result import get_result_one

class Interface_login:
    @staticmethod
    def login(method,url,data):
        response = SendMethod.send_method(method=method,url=url,data=data)
        return response



if __name__ == '__main__':
    url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signin'
    data = {"name": "lzj", "password": "admin123"}
    response = Interface.login('post',url,data)
    sid = get_result_one(response, 'sid')
    print(sid)
    uid = get_result_one(response, 'uid')
    print(uid)