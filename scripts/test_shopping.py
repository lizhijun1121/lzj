import unittest
from common.get_result import get_result_one,get_result_all
from common.db import DB
from interface.Shopping import Interface
from interface.login import Interface_login
from common.sendmethod import SendMethod

class Test_shopping(unittest.TestCase):
    def setUp(self) -> None:
        #实例化DB
        self.db = DB()
        #登录
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signin'
        data = {"name": "lzj", "password": "admin123"}
        response = Interface_login.login(method='post', url=url, data=data)
        self.sid = get_result_one(response, 'sid')
        self.uid = get_result_one(response, 'uid')


    def test_case_01(self):
        #搜索商品
        url = 'http://ecshop.itsoso.cn/ECMobile/?url=/search'
        data  ={"pagination":{"count":100,"page":1},"filter":{"keywords":"","sort_by":"price_asc","brand_id":"","category_id":"25","price_range":{"price_min":0,"price_max":0}}}
        response = Interface.search_shop(method='post',url=url,data=data)
        goods_id = get_result_all(response,'goods_id')[-10]


        #点击商品
        cli_url = 'http://ecshop.itsoso.cn/ECMobile/?url=/goods'
        cli_data = {"goods_id":goods_id,"session":{"uid":f"{self.uid}","sid":f"{self.sid}"}}
        Interface.click_shop(method='post',url=cli_url,data=cli_data)

        #加入购物车
        addcar_url = 'http://ecshop.itsoso.cn/ECMobile/?url=/cart/create'
        addcar_data = {"spec":[],"session":{"uid":f"{self.uid}","sid":f"{self.sid}"},"goods_id":goods_id,"number":1}
        addcar_response =Interface.add_shop_car(method='post',url=addcar_url,data=addcar_data)


        #选择支付方式
        check_url = 'http://ecshop.itsoso.cn/ECMobile/?url=/flow/checkOrder'
        check_data = {"session":{"uid":f"{self.uid}","sid":f"{self.sid}"}}
        check_response = Interface.check_order(method='post', url=check_url, data=check_data)
        shipping_id = get_result_all(check_response,'shipping_id')[1]
        pay_id = get_result_all(check_response,'pay_id')[1]



        # #点击提交
        submit_url = 'http://ecshop.itsoso.cn/ECMobile/?url=/flow/done'
        submit_data  ={"shipping_id":f"{shipping_id}","session":{"uid":f"{self.uid}","sid":f"{self.sid}"},"pay_id":f"{pay_id}"}
        sub_response = Interface.clikc_submit(method='post', url=submit_url, data=submit_data)
        print(SendMethod.response_dumps(sub_response))


        order_sn = get_result_one(sub_response,'order_sn')

        sql = f"select count(*) from ecs_order_info where order_sn = '{order_sn}'"
        datas = self.db.find_one(sql)
        num = datas['count(*)']
        self.assertEqual(num, 1)



if __name__ == '__main__':
    unittest.main()