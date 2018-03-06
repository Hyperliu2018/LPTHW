formatter = '%r %r %r %r'

print(formatter %(1,2,3,4)) # 格式化变量个数要一致

print(formatter % ('one','two','three','four'))

print(formatter % (True,False,False,True))

print(formatter % (formatter,formatter,formatter,formatter))

print(formatter % (
    'Thad this thing.',
    'That you could type up right.',
    "But it did't sing.",
    "So I said goodnight."
))

