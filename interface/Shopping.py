from common.sendmethod import SendMethod




class Interface:
    @staticmethod
    def search_shop(method,url,data):
        return SendMethod.send_method(method,url,data)

    @staticmethod
    def click_shop(method, url, data):
        return SendMethod.send_method(method, url, data)

    @staticmethod
    def add_shop_car(method, url, data):
        return SendMethod.send_method(method, url, data)

    @staticmethod
    def shop_car_list(method, url, data):
        return SendMethod.send_method(method, url, data)

    @staticmethod
    def update_shop_car(method, url, data):
        return SendMethod.send_method(method, url, data)

    @staticmethod
    def del_shop_car(method, url, data):
        return SendMethod.send_method(method, url, data)

    @staticmethod
    def check_order(method, url, data):
        return SendMethod.send_method(method, url, data)

    @staticmethod
    def clikc_submit(method, url, data):
        return SendMethod.send_method(method, url, data)
