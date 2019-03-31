# 실습 5
# 조건체크: 제어문(조건문: 조건)

# 논리연산자: 조건이 2개 이상인 경우,
# 하나만 true, 두개만 true..
# id 인증부분 or pw 인증부분
# id인증부분 and pw인증부분(******)

user = "root"
pw = "1234"

iUser = input("user: ")
iPw = input("pw: ")


if(user == iUser and pw == iPw):
    print("로그인 성공!")
else:
    print("로그인 실패!")
    
print("\nEND")

''' 
#산술연상자
print(3**4)

# 관계연산자(비교연산자)
a = 200
b = 100
print(a == b)  # True(참), False(거짓)
'''