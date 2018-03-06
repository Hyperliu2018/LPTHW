# this is one like your script with argv
def print_two(*args):  # 带星号*的参数为 可变参数 ，可以传入多个arguments，作为一个list
    arg1,arg2 = args
    print('arg1: %r,arg2: %r' % (arg1,arg2))

# ok that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print('arg1: %r,arg2: %r' % (arg1,arg2))

# this just takes one argument
def print_one(arg1):
    print('arg1: %r' %arg1)

# this one takes no argument
def print_none():
    print('I got nothing.')

print_two('Zed','Shaw')
print_two_again('Zed','Shaw')
print_one('First')
print_none()
