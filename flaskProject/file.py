# Author: Autumnhui

# 方法 1 （需要关闭）
# tasks = open('text.txt','a')
# print('aaa',file=tasks)
# tasks.close()


# 方法 2
# 用with语法，不用关闭
# with open('text.txt','a') as tasks:
#     print('用with写的',file=tasks)

# 用open读取文件，记得关闭
# tasks = open('text.txt')
# for list in tasks:
#     print(list,end='') #如果不写end=''有n行就会输出2n行，因为print默认空行
# tasks.close()



# 处理文件方法 'r'读   'w'写（会覆盖） 'a'写（追加）'x'打开新文件来写


