string = input()

i = 0

for i in range(len(string)):
    if((i % 10)==0 and i != 0):
        print()
    print(string[i], end='')