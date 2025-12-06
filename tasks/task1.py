# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    
    w=int(input())
    s=w//100+(w//10)%10+w%10
    print(s)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()