#!/usr/bin/env python
#-*- coding=utf-8 -*-
__author__ = "youzhanghao"

# 已知：F(0) = 0， F(1) = 1， F(n) = F(n-1) + F(n-2) 其中（n≥2，n∈N*）
def F(n):
	if n <= 1:
		return 1
	else:
		return F(n-1) * F(n-2)

for i in range(10):
	print(i,"-->",F(i))


def F_for(n):
	x,a,b = 0,0,1
	while x < n:
		a,b = b, a+b
		x += 1
		return b
for i in range(10):
	print(i,"-->",F_for(i))

g_n = [0, 1, 3, 23, 33]
def F_n(n):
	if n < 1:
		return g_n[n]
	else:
		return F_n(n-1) + g_n[n]
# F_n(0) = 0
# F_n(1) = 0 + g[1] = 1
# F_n(2) = 1 + g[2] = 4
# F_n(3) = 4 + g[3] = 27




# def f_n(n,g_n)
if __name__ == '__main__':

	for i in range(5):
		print(g_n[i], "-->", F_n(i))