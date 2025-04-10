s = 'abd'
l = ['1', 2, '3']

def add_iter(x):
    x += '!'
    print(f'{x}, x id is {id(x)}')

print(f'{l}, l id is {id(l)}')
add_iter(l)