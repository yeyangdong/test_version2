import unittest

from HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(".")   #获取当前路径下的用例，以test_开头的：源码    def discover(self, start_dir, pattern='test*.py', top_level_dir=None):


# 2.执行用例
# 创建TextTestRunner()运行器
# runner = unittest.TextTestRunner()



with open("testReport.html", "wb") as file:
    runner = HTMLTestRunner(file,
                   verbosity=1,
                   title="测试报告",
                   description="tester：yyd")
    # 3.运行套件里面的用例
    runner.run(suite)

