name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
total = age + height + weight
#inches=?

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
#total = my_age + my_height + my_weight
print(f"If I add {age}, {height}, and {weight} I get {total}")
print(f"If I add {age}, {height}, and {weight} I get total")
#如果不加{}，就只是字符串
#python格式化字符部分搜索如下
#%%	百分号标记 #就是输出一个%
#%c	字符及其ASCII码
#%s	字符串
#%d	有符号整数(十进制)
#%u	无符号整数(十进制)
#%o	无符号整数(八进制)
#%x	无符号整数(十六进制)
#%X	无符号整数(十六进制大写字符)
#%e	浮点数字(科学计数法)
#%E	浮点数字(科学计数法，用E代替e)
#%f	浮点数字(用小数点符号)
#%g	浮点数字(根据值的大小采用%e或%f)
#%G	浮点数字(类似于%g)
#%p	指针(用十六进制打印值的内存地址)
#%n	存储输出字符的数量放进参数列表的下一个变量中
