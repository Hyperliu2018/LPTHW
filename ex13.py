from sys import argv

script, first, second, third = argv # 参数解包unpack

# print('The script is called:',script)
print('Your first variable is:',first)
print('Your second variable is:',second)
print('Your third variable is:',third)

# 此脚本不能直接运行，要在命令行模式下运行，
# 且后面要加上3个参数  python C:\pytest\ex13.py first second third
