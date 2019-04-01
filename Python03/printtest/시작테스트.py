'''
# 실습 8-3 (기능 추가)
import random

# target = random! [기능추가 1]
# 입력을 하면,
# 정답이면 => 종료!
# 정답이 아니면 => 너무 커요! 너무 작아요!

# [기능추가 2] 몇 번만에 맞췄을까?


# target = random.randrange(1, 10)
target = random.randrange(1, 100)
cnt = 0
while True:
#     num = int(input("숫자를 입력[1-10],(종료:0)>> "))
    num = int(input("숫자를 입력[1-100],(종료:0)>> "))
    
    if num > 100 or num < 1:
        print("범위가 넘어가네요!!!\n-----------------")
        pass
    else:
        if num == target:
            print("(시도횟수: %d)" %cnt)
            print("맞았습니다.~!!!!!!")
            break
        elif num > target:
            print("(시도횟수: %d)" %cnt)
            print("너무 커요!\n-----------------")
        elif num < target:
            print("(시도횟수: %d)" %cnt)
            print("너무 작아요!\n-----------------")
    cnt += 1

print("\n종료합니다.")
'''

'''
# 실습 8-2

# target = 10
# 입력을 하면,
# 정답이면 => 종료!
# 정답이 아니면 => 너무 커요! 너무 작아요!

target = 5

while True:
    num = int(input("숫자를 입력[1-10],(종료:0)>> "))
    if num > 10 or num < 1:
        print("범위가 넘어가네요!!!\n-----------------")
        pass
    else:
        if num == target:
            print("맞았습니다.~!!!!!!")
            break
        elif num > target:
            print("너무 커요!\n-----------------")
        elif num < target:
            print("너무 작아요!\n-----------------")

print("\n종료합니다.")
'''

'''
# 실습 8

# target = 200
# 숫자를 입력: 150
# 틀렸습니다.
# 숫자를 입력: 210
# 틀렸습니다.
# 숫자를 입력: 200
# 맞았습니다.
# 종료합니다.


target = 200

while True:
    num = int(input("숫자를 입력(종료:0)>> "))
    if num == target:
        print("맞았습니다.~!!!!!!")
        break
    elif num == 0:
        break
    else:
        print("틀렸습니다.\n 숫자를 다시 입력해주세요.\n----------------")

print("\n종료합니다.")
'''

'''
# 실습 7
# 당신의 점수를 입력하세요.

# 60점 이상이면 합격입니다.
# 60점 미만이면, 
# - 40점 미만이면 과락 불합격
# - 아니면 그냥 불합격.

score = int(input("당신의 점수를 입력>>> "))

if score >= 60:
    print("\n합격~☆★♥♡ 캬캬캬컄!!!")
else:
    if score <= 40:
        print("\n과락 불합격 ㅠㅠㅠ")
    else:
        print("\n불합격 아아아악!!!")
'''

'''
# 실습 6-2 - 시작테스트 3
# 1. 태어난 해를 입력
# 2. 나이를 계산(year 이용)
# 3. 나이가 18살 이상이면 성년
#    -- 남, 녀 확인 
#    미만이면 미성년
#     
# 4. 프로그램 종료 처리

import datetime

# 1. 태어난 해를 입력
birth = int(input("Birth: "))
# 2. 나이를 계산(year 이용)
year = datetime.datetime.now().year
# print("year: " , year)
# print("birth: " ,birth)
age = year - birth + 1
# print("age: " ,age)

# 3. 나이가 18살 이상이면 성년
#    미만이면 미성년
if age >= 18:
    gender = input("당신의 성별은?")
    if gender == "남":
        print("\남자 성년~!!!")
    else:
        print("\n여자 성년~!!!")
else:
    print("\n미성년~!!!")
    
# 4. 프로그램 종료 처리
print("성년/미성년 판별 프로그램 종료합니다.")
'''

'''
# 실습 6 - 시작테스트 2
# 1. 태어난 해를 입력
# 2. 나이를 계산(year 이용)
# 3. 나이가 18살 이상이면 성년
#    미만이면 미성년
# 4. 프로그램 종료 처리

import datetime

# 1. 태어난 해를 입력
birth = int(input("Birth: "))
# 2. 나이를 계산(year 이용)
year = datetime.datetime.now().year
# print("year: " , year)
# print("birth: " ,birth)
age = year - birth + 1
# print("age: " ,age)

# 3. 나이가 18살 이상이면 성년
#    미만이면 미성년
if age >= 18:
    print("\n성년~!!!")
    
else:
    print("\n미성년~!!!")
    
# 4. 프로그램 종료 처리
print("성년/미성년 판별 프로그램 종료합니다.")
'''

'''
# 실습 5 - 시작테스트
# 1) 지금 몇 시인지 처리
# 2) 지금 시각이 22시 전인가요?
#     true: 아직 집에 갈 시간이 멀었군요.
#     false: 집에 갈 시각이군요.
# 시각 처리 프로그램 종료

# 1. 지금 몇 시인지 처리
import datetime

now = datetime.datetime.now()
hour = now.hour
print(hour) # 19

# 2. 지금 시각이 22시 전인가요?
#     true: 아직 집에 갈 시간이 멀었군요.
#     false: 집에 갈 시각이군요.

if hour <= 22:
    print("\n아직 집에 갈 시간이 멀었군요.")
else:
    print("\n집에 갈 시각이군요.")
#     pass
'''


'''
import datetime
import time

now = datetime.datetime.now()
print(now)
print("------")

time.sleep(2)   # 재우기
print(now.year)
print(now.month)
print(now.day)
print(now.weekday()) # 0: 월요일
print('월화수목금토일'[now.weekday()]) # 0: 월요일
print(now.hour)
print(now.minute)
print(now.second)
'''
