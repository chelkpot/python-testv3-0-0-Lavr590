# tasks/task5.py

def solve():
# Ниже пишите решение задачи

    v=int(input())
    hours=v//3600%24
    minutes=(v//60)%60
    seconds=v%60
    print(hours,":",minutes//10,minutes%10,":", seconds//10,seconds%10,sep="")
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()