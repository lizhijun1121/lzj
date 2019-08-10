from common.get_result import get_result_one
from interface.interface import Interface

class Login():
    @staticmethod
    def login():
        """登录"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        method = "post"
        req_data = {"name": "lzj", "password": "admin123"}
        response = Interface.login(method=method, url=url, data=req_data)
        sid = get_result_one(response, "sid")
        uid = get_result_one(response, "uid")
        return sid, uid
