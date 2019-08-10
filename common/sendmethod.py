import requests,json


class SendMethod:
    @staticmethod
    def send_method(method,url,data):
        req_data = {'json':json.dumps(data)}
        if method == 'post':
            response = requests.request(method ='post',url=url,data=req_data)
        elif method == 'get':
            response = requests.request(method='get', url=url)
        else:
            response = None
        return response.json()

    @staticmethod
    def response_dumps(response):
        return json.dumps(response,indent=3,ensure_ascii=False)


if __name__ == '__main__':
    url = 'http://ecshop.itsoso.cn/ECMobile/?url=/user/signin'
    data = {"name":"lzj","password":"admin123"}
    response = SendMethod.send_method(method='post',url=url,data=data)
    print(SendMethod.response_dumps(response))
