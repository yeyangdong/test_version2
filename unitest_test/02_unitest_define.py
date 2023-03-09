# 0.导入unittest模块
import unittest
from unitest_test.handle_request import HandleRequest


#1.需要继承unittest.TestCase父类
class TestRegister(unittest.TestCase):
    #2.创建测试用例测试方法，一定要以test_作为前缀
    def test_register_success(self):
        #3.构造请求参数
        do_requset = HandleRequest()
        register_url = "http://api.lemonban.com:8788/futureloan/member/register"
        header_dict = {
            "X-Lemonban-Media-Type": "lemonban.v2",
            "User-Agent": "Mozilla/5.0 LookSky",
            "Content-Type": "application/json"
        }
        do_requset.add_headers(header_dict)
        requests_params = {
            "mobile_phone": "15158787632",
            "pwd": "12345678",
            "reg_name": "",
            "type": 0
        }


        #4.向接口发起请求
        res = do_requset.send(method="post", url=register_url, json=requests_params)


        #5.断言
        expected_value = 0
        real_code = res.json()["code"]

        # if expected_value == real_code:
        #     print("success")
        # else:
        #     print("false")
        self.assertEqual(expected_value,real_code)




if __name__ == '__main__':
    unittest.main()    # 这个也会执行该文件下的所有用例
