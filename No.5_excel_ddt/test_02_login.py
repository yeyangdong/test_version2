# 0.导入unittest模块
import unittest
from handle_request import HandleRequest
from handle_excel import HandleExcel

# 1.需要继承unittest.TestCase父类
class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 所有用例执行，也只会调用一次
        print("\nsetUPClass")
        cls.do_request = HandleRequest()
        cls.url = "http://api.lemonban.com:8788/futureloan/member/login"
        header_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky",
            "Content-Type": "application/json"
        }
        cls.do_request.add_headers(header_dict)

    @classmethod
    def tearDownClass(cls):
        print("\ntearDownClass")
        cls.do_request.close()





    def test_01_login_success(self):
        requests_params = {
            "mobile_phone": "15158787632",
            "pwd": "12345678",
            "reg_name": "",
            "type": 0
        }
        # 4.向接口发起请求
        res = self.do_request.send(method="post", url=self.url, json=requests_params)
        # 5.断言
        expected_value = "token_info"
        # actual = res.json()["code"]
        try:
            self.assertEqual(expected_value,res.text,'{"code":2,"msg":"账号已存在","data":null,"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"}')
        except AssertionError as e:
            print("此处需要日志记录")
            print(f"具体异常为：{e}")
            raise e

    def test_02_no_pwd(self):
        requests_params = {
            "mobile_phone": "15158787632",
            "pwd": "",
            "reg_name": "",
            "type": 0
        }

        # 4.向接口发起请求
        res = self.do_request.send(method="post", url=self.url, json=requests_params)

        # 5.断言
        expected_value = "1"
        try:
            self.assertEqual(expected_value,res.text,"密码为空")
        except AssertionError as e:
            print("此处需要日志记录")
            print(f"具体异常为：{e}")
            # raise e

if __name__ == '__main__':
    unittest.main()  # 这个也会执行该文件下的所有用例
