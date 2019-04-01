# 실습 1
# 함수 만들기.
# 1) 두 값 입력받아서, 합계 내어 반환 받아 프린트!
# 2) 합계 받은 값에서 10을 뺀 값을 반환받아 프린트!
def tot(x, y):
    return x + y

def subt(var):
    return var - 10

a = int(input("a>> "))
b = int(input("b>> "))

print("두 수의 합 = %d" %tot(a, b))
print("두 수의 합 -10= %d" %subt(tot(a, b)))


'''
# p.83~84 함수
def sum(x, y):
#     print(x + y)
    return (x + y)
    
     
a = sum(200, 100)
print(a)
print("반환 받은 값>>", a)
print("반환 받은 값>>%d" %a)
'''

'''
# p.69 ~ 72

a = 100

b = a

print(a)
print(b)

print()
a = b = 200
print(a)
'''