print('How old are you?')
age = input()  # python2 中input和raw_input 整合了，python3没有了raw_input
print('How tall are you?')
height = input()
print('How much do you weight?')
weight = input()

print('So, you\'re %r old, %r tall and %r heavy.' % (age,height,weight))

