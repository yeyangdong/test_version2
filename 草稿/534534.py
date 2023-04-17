# tuple1 = {"姓名": 'a', "年龄": 'b', "籍贯": 'c'}
# tuple2 = {"姓名": 'd', "年龄": 'e', "籍贯": 'f'}
#
#
# print(tuple1.items())


# import requests #导入requests包
# url = 'http://www.baidu.com'
# strhtml = requests.get(url) #Get方式获取网页数据
# print(strhtml.text)


# import requests
#
# class tet():
#     def English_Chinese(self):
#         url = "https://fanyi.baidu.com/sug"
#         s = input("请输入要翻译的词(中/英):")
#         dat = {
#             "kw": s
#         }
#         resp = requests.post(url, data=dat)  # 发送post请求
#         ch = resp.json()  # 将服务器返回的内容直接处理成json => dict
#         resp.close()
#         dic_lenth = len(ch['data'])
#         for i in range(dic_lenth):
#             print("词:" + ch['data'][i]['k'] + " " + "单词意思:" + ch['data'][i]['v'])
#
# if __name__ == '__main__':
#     ter = tet()
#     ter.English_Chinese()


for i in range(1,10):
    print(i)
