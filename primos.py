MAX = 10000000

# criba de primos
primo = [True]*(MAX+1)
primo[0] = primo[1] = False

for i in range(2, int(MAX**0.5)+1):
    if primo[i]:
        for j in range(i*i, MAX+1, i):
            primo[j] = False

# arreglo acumulado para contar rápido
acum = [0]*(MAX+1)
for i in range(1, MAX+1):
    acum[i] = acum[i-1] + (1 if primo[i] else 0)

# leer datos
t = int(input())

for _ in range(t):
    a, b = map(int,input().split())
    print(acum[b] - acum[a-1])