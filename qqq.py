# -*- coding:UTF-8 -*-
# ###测试python输出中文是否乱码
import json
print u'哈哈你好'
string='哈哈你好'
print string.decode('UTF-8')
t_tuple=('哈哈','你好')
t_list=['哈哈','你好']
t_dict={1:'哈哈',2:'你好'}
print json.dumps(t_tuple,encoding='UTF-8',ensure_ascii=False)
print json.dumps(t_list,encoding='UTF-8',ensure_ascii=False)
print json.dumps(t_dict,encoding='UTF-8',ensure_ascii=False)
