# tasks/task2.py

def solve():
# Ниже пишите решение задачи

    z=int(input())
    z=z%1440
    chas=z//60
    minuta=z%60
    print(chas, minuta)

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()