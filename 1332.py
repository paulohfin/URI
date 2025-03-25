n = int(input())
for i in range(n):
    num = input()
    if len(num) > 3:
        print(3)
    else:
        if (num[0] == 'o' and num[1] == 'n') or (num[0] == 'o' and num[2] == 'e') or (num[1] == 'n' and num[2] == 'e'):
            print(1)
        else:
            print(2)