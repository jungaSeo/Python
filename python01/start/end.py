'''
Created on 2019. 3. 28.

@author: zzang
'''
dept = input("소속: ")
subj = input("과목: ")


bScore = input("지난번 성적: ")
tScore = input("이번 성적: ")

bScoreInt = int(bScore)
tScoreInt = int(tScore)

print("your input dept is ", dept)
print("your input subj is ", subj)

finalScore = bScoreInt + tScoreInt
print("your final score is", finalScore)