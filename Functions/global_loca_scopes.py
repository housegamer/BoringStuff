#global scope
spam = 22

def eggs():
    #local scope
    spam = 11
    return spam
print(spam)
print(eggs())