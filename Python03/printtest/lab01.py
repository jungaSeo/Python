# 정리문제
# 자판기 프로그램을 구현(순서도 + 구현)
# 기능정의
# 0) 종료할 때까지 계속 고를 수 있음.
import random

# 1) 물건을 고르고
# 2) 돈을 입력 후 
# 3) 잔돈을 계산


def buyProduct():
    global pAmount
    global change
    pCnt = int(input("구매 수량>>> "))
    
    pAmount += random.randrange(1, 10000) * pCnt
    if pAmount > money:
        print("가진 금액보다 구매금액이 큽니다. 수량 재 설정 해주세요~!!!\n")
        pAmount = money - change
    else:    
        change = money - pAmount
    print("현재 구매 대금: %d\n" %pAmount)

    
def calc():
    print("보유 금액: %10d" %money)
    print("구매 금액: %10d" %pAmount)
    print("       잔돈: %10d" %change)


global money
money = int(input("보유 금액>>> "))
change = money
pAmount = pCnt = 0


while(True):
    opt = int(input("[0.종료(계산), 1.구매] : "))
    print("----------------------")
    if opt == 0 or change <= 1000:
        calc()
        break
    elif opt == 1:
        buyProduct()
    else: 
        print("잘못 누르셨습니다.\n---------------")        
        