n = int(input())

h = int(n/3600)
n-=h*3600
min = int(n/60)
n-=min*60
print(f'{h}:{min}:{n}')