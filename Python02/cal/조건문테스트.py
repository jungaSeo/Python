# 실습 9

# 자장면 한 그릇 가격 4500원
# 짬봉 한 그릇 가격 3000원
# ------------------
# 자장면 주문 수: 5
# 짬봉 주문 수: 3
# -----------------
# 자장면 금액, 짬봉 금액, 전체주문 금액 출력

f1 = 4500
f2 = 3000
print("자장면 한 그릇 가격  4500원\n 짬봉 한그릇 가격 3000원")

print("------------------------")
numf1 = int(input("자장면 주문 수: ")) 
numf2 = int(input("짬봉 주문 수: "))

print("------------------------")
print("자장면 금액:", f1 * numf1)
print("짬봉 금액:", f2 * numf2)
print("전체주문 금액:", (f1 * numf1) + (f2 * numf2))
print("------------------------") 



'''
# 실습 8

# 교보문고
# 1000원짜리 스티커 3장, 2500원짜리 책갈피 4개
# 우수회원 할인으로 10% 할인. 내가 낸 금액 얼마?

ranking = 1 # 1: 우수, 2: 기본

sticker = 1000
bookmark = 2500

stickerNum = int(input("스티커 구매 수량: "))
bookmarkNum = int(input("책갈피 구매 수량: "))

total = ((sticker * stickerNum) + (bookmark * bookmarkNum))

if ranking == 1:
    result = total - (total * 0.1)
else:
    result = total

print("총계: ", round(result))
print("\nEND")
'''


'''
# 실습 7

# 자장면 한 그릇 4500원
# 일행 5명 => 2000원 할인
# 아니면 할인 안해줌!
# 우리가 낸 금액 얼마?

food = 4500

pep = int(input("일행 수>> "))
if pep >= 5:
    price = (4500 * pep)-2000
else :
    price = 4500 * pep

print("총계: ", price)
print("\nEND")
'''


'''
# 실습 6

# 키보드 입력 정수 홀수, 짝수 구분 pg
num = int(input("정수를 입력하시오: "))

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
print("End")    

'''    

'''
# 실습 4

# 사원이 실적 목표를 달성하였을 경우 실적 목표를 초과한 금액의 10% 성과급으로 받는 pg
aim = 1000
profit = int(input("실적(단위:만원): "))
print()
if profit > aim :
    print("실적달성")
    print("보너스:", (profit-aim)*0.1)
else:
    print("분발하세요~!!")
print("End")    
'''
    

'''
# 실습 3

# 두 수를 입력받는다.
# 더 큰 숫자를 찾기!

num1 = int(input("숫자1> "))
num2 = int(input("숫자2> "))

if num1 > num2 :
    print(num1, "이 더 큼!")
else:
    print(num2, "이 더 큼!")
    
print("End~~")
'''


'''
# 실습  2

# 한 수 입력. 이 수가 100보다 작으면, 100보다 작은 숫자가 들어왔군요. 출력
# 프로그램이 끝났습니다.

num = int(input("숫자입력> "))

if num < 100 :
    print("100 보다 작음!")
else:
    # pass # 처리 내용 미정..
    print("100 보다 큼!")

print("프로그램이 끝났습니다.")
'''


'''
# 조건문 문법

data = 99

if data < 100 :
    print("조건 ok!")
'''
