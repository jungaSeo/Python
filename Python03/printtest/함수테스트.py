# # 메인 코드 부분
# if __name__ == '__main__':
#     print('메인 함수 부분이 실행됩니다.')


# 실습 3

# 입력받는 함수 1개 + 개수 세는 함수 여러개
# 56789원 입니다.
# 1000원짜리 몇 개? 56개
# 500원짜리 몇 개? 1개
# 100원짜리 몇 개? 2개
# 10원짜리 몇 개? 8개
# 1원짜리 몇 개? 9개

def countFunc(x):
    remain = x
    for i in range(0, 5):
        mok[i] = int(remain / div[i]) # ==  remain // div[i]
        remain = remain % div[i]
#         print(i,".remain", remain)
#     return mok

mok = [0, 0, 0, 0, 0]
div = [1000, 500, 100, 10, 1]


intSum = int(input("총 계: ")) # intSum = 56789
countFunc(intSum)
print()
for i in range(0, 5):
    print("%d원짜리 개수: %d개" %(div[i], mok[i]))
#     print("mok[",i,"]= ", mok[i])
     
# print(int(tot / 1000))
# print(56789 % 1000)




'''
# 실습 2

# 1) 입력받는 함수 정의
# 좋아하는 색은(빨강:1, 노랑:2, 파랑:3)
# 2) 입력받은 값을 반환받아,
# 1이면, 파이썬 스터디반.
# 2   , 장고 스터디반.
# 3   , 웹 구축 스터디반.


def inputColor():
    intColor = int(input("좋아하는 색은(빨강:1, 노랑:2, 파랑:3)>> "))
    return intColor

def outputStudy(x):
    if x == 1:
        return "파이썬 스터디반"
    elif x == 2:
        return "장고 스터디반"
    else:
        return "웹 구축 스터디반"
      
intCol = inputColor()
print("스터디반: ", outputStudy(intCol))
'''    



# 인원, 가격, 입력을 받아서 두 수를 곱한 후, 
# 곱한 수가 10000원이 넘으면, 2000원을 할인
'''
def inputFunc():
    person = int(input("인원 입력>> "))
    price = int(input("가격 입력>> "))
    return person * price
#     print(person, "", price)

def process(x):
    if x >= 10000: 
        x -= 2000
    else:          
        x
    return x
    

# print("두 수를 곱한 값: ", inputFunc())
result = inputFunc()
print("\n두 수를 곱한 값: ", result)

total = process(result)
print("당신이 지불할 금액은: ", total)
'''