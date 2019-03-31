'''
# 5. 
# input: 이름, 나이, 소속 =>  출력

name = input("당신의 이름은:")
age = int(input("당신의 나이는:"))
dept = input("당신의 소속은:")
print("------------------------------")
print("당신의 이름은", name, "당신의 나이는", age, "당신의 소속은:", dept)
'''

'''
# 4. 

# 키보드 가격: 4000
# 키보드 갯수:
# 마우스 가격: 3000
# 마우스 갯수: 
# 키보드 총 가격, 마우스 총 가격, 제품 총 가격

keyboard = 4000
mouse = 3000
print("키보드 가격: 4000")
keyboardNum = int(input("키보드 갯수: "))
print("마우스 가격: 3000")
mousedNum = int(input("마우스 갯수: "))
print("-----------------------------")
print("키보드 총 가격:", keyboard*keyboardNum)
print("마우스 총 가격:", mouse*mousedNum)
print("제품 총 가격:", (keyboard*keyboardNum)+(mouse*mousedNum))
'''


'''
# 3. 다음의 영수증 출력.(부가세는 10%)

amount = int(input("받은 돈: "))
goodsPrice = int(input("상품의 총액: "))

print("부가세: ", round(goodsPrice*0.1))
print("잔돈: ", amount-goodsPrice)
'''


'''
# 2. 두 수를 입력받아 같은지 비교, 같으면 "두 수가 같습니다. 
# 다르면 "두 수가 다릅니다."

num1 = int(input("num1>> "))
num2 = int(input("num2>> "))

if num1 == num2:
    print("두 수가 같습니다")
else:
    print("두 수가 다릅니다")
'''


'''
# 1.
# 기온, 평가, 신발사이즈 입 출력

print("----------------------")
temp = float(input("오늘의 기온은? "))
rank = input("오늘 나의 평가는? ")
size = float(input("나의 신발 사이즈는? "))
print("----------------------")

print("오늘은", temp,"도, 나의 평가는", rank,", 신발은", size)
'''