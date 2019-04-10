import json

#1. 定义一个json 字典数据
json_dic = {"username":"xiaohong", "tel":"121214", "email":["qwe@qq.com", "wer@2.com"]}
print("Type of json_dic: %s" % type(json_dic))

#2。将一个字典数据通过json。dumps方法转化成字符串
json_str = json.dumps(json_dic)
print("Type of json_str: %s" % type(json_str))
print("Content of json_str: %s" % json_str)

#3。 将一个字符串，通过json。loads方法转化成字典
str2 = '''{"username": "xiaohong", "tel": "121214", "email": ["qwe@qq.com", "wer@2.com"]}'''
json_str_2_dic = json.loads(str2)
print("Type of json_str_2_dic: %s" % type(json_str_2_dic))
