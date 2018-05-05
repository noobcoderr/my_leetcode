a = 123
if a < 0:
    abs_a = abs(a)
str_a = str(abs_a)
lists = list(str_a)
lists.reverse()
print(lists)
while lists[0] == '0':
    del lists[0]
result = ''.join(lists)
result = int(result)
if a < 0:
    result = -result
print(result)
    

