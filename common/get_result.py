import jsonpath

def get_result_one(data,keyword):
    return jsonpath.jsonpath(data,f'$..{keyword}')[0]

def get_result_all(data,keyword):
    return jsonpath.jsonpath(data,f'$..{keyword}')


if __name__ == '__main__':
    data = {
   "data": [
      {
         "order_id": "2412",
         "order_sn": "2019072359563",
         "order_time": "2019/07/23 13:12:24 +0800",
         "total_fee": "￥17.50元",
         "goods_list": [
            {
               "goods_id": "35",
               "name": "体重秤",
               "goods_number": "1",
               "subtotal": "￥14.00元",
               "formated_shop_price": "￥14.00元",
               "img": {
                  "small": "http://ecshop.itsoso.cn/images/201605/thumb_img/35_thumb_G_1462851036709.jpg",
                  "thumb": "http://ecshop.itsoso.cn/images/201605/goods_img/35_G_1462851036470.jpg",
                  "url": "http://ecshop.itsoso.cn/images/201605/source_img/35_G_1462851036185.jpg"
               }
            }
         ],
         "formated_integral_money": "￥0.00元",
         "formated_bonus": "￥0.00元",
         "formated_shipping_fee": "￥3.50元",
         "order_info": {
            "pay_code": "yunqi",
            "order_amount": "17.50",
            "order_id": "2412",
            "subject": "体重秤等1种商品",
            "desc": "体重秤等1种商品",
            "order_sn": "2019072359563"
         }
      },
      {
         "order_id": "2411",
         "order_sn": "2019072381566",
         "order_time": "2019/07/23 13:08:00 +0800",
         "total_fee": "￥3.50元",
         "goods_list": [
            {
               "goods_id": "85",
               "name": "索尼 Xperia 1",
               "goods_number": "1",
               "subtotal": "￥0.00元",
               "formated_shop_price": "￥0.00元",
               "img": {
                  "small": "http://ecshop.itsoso.cn/images/201903/thumb_img/85_thumb_G_1553164759715.jpg",
                  "thumb": "http://ecshop.itsoso.cn/images/201903/goods_img/85_G_1553164759968.jpg",
                  "url": "http://ecshop.itsoso.cn/images/201903/source_img/85_G_1553164759229.jpg"
               }
            }
         ],
         "formated_integral_money": "￥0.00元",
         "formated_bonus": "￥0.00元",
         "formated_shipping_fee": "￥3.50元",
         "order_info": {
            "pay_code": "alipay",
            "order_amount": "3.50",
            "order_id": "2411",
            "subject": "索尼 Xperia 1等1种商品",
            "desc": "索尼 Xperia 1等1种商品",
            "order_sn": "2019072381566"
         }
      }
   ],
   "status": {
      "succeed": 1
   },
   "paginated": {
      "total": 2,
      "count": 2,
      "more": 0
   }
}

    print(get_result_one(data, 'order_id'))

