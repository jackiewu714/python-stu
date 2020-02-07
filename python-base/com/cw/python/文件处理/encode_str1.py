# coding=utf-8
import time

str_module = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$_"
list_module = list(str_module)
while True:
	str = list(input("请输入解码字符串:60665\n"))
	total = 0
	num = str.__len__() - 1
	for sr in str:
		for i in range(list_module.__len__()):
			s = list_module[i]
			if sr == s:
				total = total+64**(num)*i
				num = num-1
	print('解码后字符串：%s'%total)