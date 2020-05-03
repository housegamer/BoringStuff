'''spam = 0
while spam < 5:
    print('hi')
    spam += 1
'''
'''
name = ''
while name != 'your name':
    print('enter ur name')
    name = input()
print('ty')
'''
'''name = ''
while True:
    print('print ur name')
    name = input()
    if name =='ur name':
        break
print('ty')
'''

spam = 0

while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print(f'spam is {spam}')