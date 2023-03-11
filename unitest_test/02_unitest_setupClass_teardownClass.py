# 0.导入unittest模块
import unittest
from unitest_test.handle_request import HandleRequest


#1.需要继承unittest.TestCase父类
class TestRegister(unittest.TestCase):
    def setUp(self):
        # 实例方法有几个，就执行几次setUp和tearDown
        # 先执行setUp，在执行用例，最后执行tearDown
        # 往往用于用例的初始化，一些前置操作
        print("\nsetUP")
        self.do_requset1 = HandleRequest()
        self.register_url = "http://api.lemonban.com:8788/futureloan/member/register"
        header_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky",
            "Content-Type": "application/json"
        }
        self.do_requset1.add_headers(header_dict)

    def tearDown(self):
        # teardown主要的用处可以是标记为用例执行结束了，但是在技术层面，主要是为了close关闭，释放资源
        print("tearDown")
        self.do_requset1.close()
        pass


    def test_register_success(self):
        requests_params = {
            "mobile_phone": "15158787632",
            "pwd": "12345678",
            "reg_name": "",
            "type": 0
        }

        #4.向接口发起请求
        res = self.do_requset1.send(method="post", url= self.register_url, json=requests_params)


        #5.断言
        self.assertIn('{"code":2,"msg":"账号已存在","data":null,"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"}',res.text)


    def test_no_mobile(self):
        requests_params = {
            "mobile_phone": "",
            "pwd": "12345678",
            "reg_name": "",
            "type": 0
        }


        #4.向接口发起请求
        res = self.do_requset1.send(method="post", url=self.register_url, json=requests_params)

        #5.断言
        self.assertIn('{"code":1,"msg":"手机号为空","data":null,"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"}',res.text)

if __name__ == '__main__':
    unittest.main()    # 这个也会执行该文件下的所有用例
