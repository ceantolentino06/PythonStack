import random
def randInt(min=0, max=100):
    if min>max:
        return 'Invalid numbers'
    if max < 0:
        return 'Invalid numbers'
    return round(random.random() *  max) + min

print(randInt(-6, 3))