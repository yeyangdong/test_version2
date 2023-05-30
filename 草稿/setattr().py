class A(object):
    bar = 1


a = A()
getattr(a, 'bar')  # 获取属性 bar 值
print(a.bar)
# 1



setattr(a, 'bar', 5)       # 设置修改属性 bar 值
a.bar
print(a.bar)
# 5