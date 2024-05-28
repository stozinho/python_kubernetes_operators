import itertools

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    

cartesian = [list(i) for i in itertools.product(range(x+1), range(y+1), range(z+1)) if sum(i) != n]

print(cartesian)