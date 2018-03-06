x ='There are %d types of people.' % 10

binary = 'binary'

do_not = "don't"

y = 'Those who know %s and those who %s.' % (binary,do_not)
# 格式化字符串：将formatted variables放在字符串中，在字符串后面跟着%， 再跟变量：% variable；
# 如果是多个变量，那么在% 后面用（）把多个变量括起来，用逗号隔开
print(x)

print(y)

print('I said: %r.' % x)
print("I also said:'%s'. " % y)

hilarious = False

joke_evaluation = "Isn't that joke so funny?! % r"

print(joke_evaluation % hilarious)

w = 'This is the left side of ...'
e = 'a string with a right side.'
print(w + e)
