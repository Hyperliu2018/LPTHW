from sys import argv

script,filename = argv # 执行代码时，命令行要输入两个参数。
# sys.argv 用来获取命令行参数
# Python 中也可以所用 sys 的 sys.argv 来获取命令行参数：
# sys.argv 是命令行参数列表。len(sys.argv) 是命令行参数个数。
# 注：sys.argv[0] 表示脚本名。

txt = open(filename) # 打开文件
# 代码执行前，要新建该文件，此处的文件名是代码执行的输入的名称

print("Here's your file %r:" % filename)
print(txt.read())  # 读取文件，并打印文件内容

print('Type the filename again:')
file_again = input('>')  # 提示输入

txt_again = open(file_again)

print(txt_again.read())

# 注：代码文件ex15.py 和文本文件ex15_sample.txt 要放在同一个文件夹中；
# 在命令行中执行时，先把目录切换到代码所在的文件  cd C:\pytest ,若果不切换目录，执行时文件名前要添加文件路径
# 然后再用python ex15.py ex15_sample.txt命令执行。
