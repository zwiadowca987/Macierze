# Macierz A

print('Rozmiar Macierzy: ')
x1=int(input())
y1=int(input())

tab=[]

print('Wartości:')

for i in range(x1):
    temp=[]
    for j in range(y1):
        temp.append(int(input()))
    tab.append(temp)

print()

# Macierz B

print('Rozmiar Macierzy: ')
x2=int(input())
y2=int(input())

tab2=[]

print('Wartości:')

for i in range(x2):
    temp=[]
    for j in range(y2):
        temp.append(int(input()))
    tab2.append(temp)

print('\n')

# Wypisanie

print('Macierz A:')

for i in range(x1):
    print('|',end='')
    for j in range(y1):
        print(tab[i][j],end='')
        if j<y1-1:
            print('\t',end='')
    print('|')

print()

print('Macierz B:')

for i in range(x2):
    print('|',end='')
    for j in range(y2):
        print(tab2[i][j],end='')
        if j<y2-1:
            print('\t',end='')
    print('|')

print()

# Dodawanie Macierzy

if x1==x2 and y1==y2:
    print('Macierz C = A + B:')

    for i in range(x1):
        print('|',end='')
        for j in range(y1):
            print(tab[i][j]+tab2[i][j],end='')
            if j<y1-1:
                print('\t',end='')
        print('|')
else:
    print('Dodanie macierzy o różnych wymiarach jest niemożliwe.')

print()

# Mnożenie Macierzy

if x1==y2 and y1==x2:
    print('Macierz D = A * B:')

    tab3=[]

    for i in range(x1):
        temp=[]
        for j in range(y2):
            temp2=0
            for k in range(y1):
                temp2+=tab[i][k]*tab2[k][j]
            temp.append(temp2)
        tab3.append(temp)

    for i in range(x1):
        print('|',end='')
        for j in range(y2):
            print(tab3[i][j],end='')
            if j<y2-1:
                print('\t',end='')
        print('|')
else:
    print('Mnożenie macierzy o nieodpowiednich wymiarach jest niemożliwe.')
