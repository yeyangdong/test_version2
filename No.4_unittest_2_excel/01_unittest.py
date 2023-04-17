import unittest

from test_01_register import TestRegister
from unittest_2_excel.test_02_login import Testlogin


# 1.创建TestSuite套件对象
#   相当于一个袋子，装测试用例
suit = unittest.TestSuite()


# 2.创建一个TestLoader加载器对象
#   创建工人
loader = unittest.TestLoader()


# 使用TestSuite套件对象.addTest来加载用例
# 使用TestLoader对象.loadTestsFromTestCase来添加测试类（testCase的子类）
suit.addTest(loader.loadTestsFromTestCase(TestRegister))
suit.addTest(loader.loadTestsFromTestCase(Testlogin))


# 3.执行用例
# 创建TextTestRunner运行期
runner = unittest.TextTestRunner()
runner.run(suit)
pass