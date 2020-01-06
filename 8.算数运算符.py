#加+
#减——
#乘*
#除：浮点除法/    1.取整//     2.取余%
#指数**
#输入2个数字，计算各个结果

#输入数字
num1 = int(input("请输入数字a:"))
num2 = int(input("请输入数字b:"))
ret1 = num1 + num2
ret2 = num1 - num2
ret3 = num1 * num2
ret4 = num1 / num2
ret5 = num1 // num2
ret6 = num1 % num2
ret7 = num1 ** num2
#输出数字
print("数字之和为：%d" % ret1)
print("数字之差为：%d" % ret2)
print("数字之和为：%d" % ret3)
print("数字之商为：", ret4)
print("数字取整：%d" % ret5)
print("数字取余数：%d" % ret6)
print("指数结果为：%d" % ret7)


