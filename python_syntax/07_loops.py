#############################################################
#                                                           #
#                           반복문                            #
#                                                           #
#############################################################

# 1) For 와 In 구문 (반복문)

# [기본 문법]

# for 하나씩 꺼내올 때 변수 in [꺼내올 집합]:

# (indent)

# list, tuple, set, dictionary, 문자열 형태 모두 가능

# range와 결합하여 사용 가능

# 리스트(list)
mylist = [1, 2, 3, 4, 5]
# # 코드를 입력해 주세요
for i in mylist:
    print(i)
# [출력]
# 1
# 2
# 3
# 4
# 5

# 튜플(tuple)
for i in (1, 2, 3, 4, 5):
    print(i)
# [출력]
# 1
# 2
# 3
# 4
# 5

# tuple + list

# tuple을 전체로 받아주는 경우

person = ('제이콥스', 10)
print(person)
print(person[0])
print(person[1])

# [출력]
# ('제이콥스', 10)
# 제이콥스
# 10

# tuple의 요소를 개별로 받아주는 경우

name, age = ('제이콥스', 10)
print(name)
print(age)

# [출력]
# 제이콥스
# 10

# 반복문에서의 응용

mytuplelist = [('제이콥스', 10), ('피터', 20), ('타이거', 30)]

for mytuple in mytuplelist:
    print(mytuple[0], mytuple[1])
# [출력]
# 제이콥스 10
# 피터 20
# 타이거 30

mytuplelist = [('제이콥스', 10), ('피터', 20), ('타이거', 30)]

for name, age in mytuplelist:
    print(name, age)
# [출력]

# 제이콥스 10
# 피터 20
# 타이거 30

# 딕셔너리(dictionary)
mydict = {'헐크': 50, '아이언맨': 60, '펭수': 70}
for key in mydict.keys():
    print(key)
    print(mydict[key])
# [출력]
# 헐크
# 아이언맨
# 펭수

for value in mydict.values():
    print(value)
# [출력]
# 50
# 60
# 70

print(mydict.items())
for name, age in mydict.items():
    print(name, age)

# [출력]
# 헐크 50
# 아이언맨 60
# 펭수 70

# 문자열(str)
for c in "Hello":
    print(c)
# [출력]
# H
# e
# l
# l
# o

# range()

# range() 함수는 별도의 list, tuple 생성 없이 range() 에서 정의한 범위를 반복하는데 활용할 수 있습니다.

# range(start, stop, step) 형식을 사용합니다.

# stop: 단일 값을 지정하는 경우

for i in range(10):
    print(i)
# [출력]

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# start, stop: 두 개의 값을 지정한 경우

for i in range(2, 9):
    print(i)
# [출력]

# 2
# 3
# 4
# 5
# 6
# 7
# 8
# start, stop, step: 세 개의 값을 지정한 경우

for i in range(1, 10, 2):
    print(i)
# [출력]


# 1
# 3
# 5
# 7
# 9

# 반복문의 중첩
for i in range(1, 4):
    for j in range(1, 4):
        print(f'(i={i}) * (j={j}) = {i * j}')
    print('===')
# [출력]

# (i=1) * (j=1) = 1
# (i=1) * (j=2) = 2
# (i=1) * (j=3) = 3
# ===
# (i=2) * (j=1) = 2
# (i=2) * (j=2) = 4
# (i=2) * (j=3) = 6
# ===
# (i=3) * (j=1) = 3
# (i=3) * (j=2) = 6
# (i=3) * (j=3) = 9
# ===

################################################################################################################################

# 연습문제

# 반복문과 조건문을 활용하여 sample 에서 음수 값만 출력해 주세요

sample = [1, 11, 22, -20, 55, -33, 0, -5, 12, 35, 19, -9, -1, -100, 90]
# # 코드를 입력해 주세요
for i in sample:
    if i < 0 :
        print(i)
# [출력]

# -20
# -33
# -5
# -9
# -1
# -100

# 반복문과 조건문을 활용하여 sample의 요소 중 10보다 크고 50보다 작은 요소만 출력해 주세요

# # 코드를 입력해 주세요
for i in sample:
    if i > 10 and i < 50 :
        print(i)
# [출력]

# 11
# 22
# 12
# 35
# 19

# 다음의 문자열을 반복문을 활용하여 출력하되, 모음('a', 'e', 'i', 'o', 'u')만 대문자로 자음은 소문자로 출력해 주세요.

sample = "PyThoN Is fUn"
# # 코드를 입력해 주세요
for i in sample.lower() :
    if i in ['a', 'e', 'i', 'o', 'u']:
        print(i.upper())
    else:
        print(i)
    
# [출력]


#  p
#  y
#  t
#  h
# (모음) O
#  n
# (공백) 
# (모음) I
#  s
# (공백) 
#  f
# (모음) U
#  n


# 구구단을 반복문을 사용하여 만들어 보세요!

# 구구단은 2단 부터 9단까지 있습니다.

# # 코드를 입력해 주세요
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')
    print()
# [출력]

# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# 2 X 4 = 8
# 2 X 5 = 10
# 2 X 6 = 12
# 2 X 7 = 14
# 2 X 8 = 16
# 2 X 9 = 18


# 3 X 1 = 3
# 3 X 2 = 6
# 3 X 3 = 9
# 3 X 4 = 12
# 3 X 5 = 15
# 3 X 6 = 18
# 3 X 7 = 21
# 3 X 8 = 24
# 3 X 9 = 27


# 4 X 1 = 4
# 4 X 2 = 8
# 4 X 3 = 12
# 4 X 4 = 16
# 4 X 5 = 20
# 4 X 6 = 24
# 4 X 7 = 28
# 4 X 8 = 32
# 4 X 9 = 36


# 5 X 1 = 5
# 5 X 2 = 10
# 5 X 3 = 15
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# 5 X 8 = 40
# 5 X 9 = 45


# 6 X 1 = 6
# 6 X 2 = 12
# 6 X 3 = 18
# 6 X 4 = 24
# 6 X 5 = 30
# 6 X 6 = 36
# 6 X 7 = 42
# 6 X 8 = 48
# 6 X 9 = 54


# 7 X 1 = 7
# 7 X 2 = 14
# 7 X 3 = 21
# 7 X 4 = 28
# 7 X 5 = 35
# 7 X 6 = 42
# 7 X 7 = 49
# 7 X 8 = 56
# 7 X 9 = 63


# 8 X 1 = 8
# 8 X 2 = 16
# 8 X 3 = 24
# 8 X 4 = 32
# 8 X 5 = 40
# 8 X 6 = 48
# 8 X 7 = 56
# 8 X 8 = 64
# 8 X 9 = 72


# 9 X 1 = 9
# 9 X 2 = 18
# 9 X 3 = 27
# 9 X 4 = 36
# 9 X 5 = 45
# 9 X 6 = 54
# 9 X 7 = 63
# 9 X 8 = 72
# 9 X 9 = 81

####################################################################################

# 2) 제어문, While

# 제어문
# continue
# 반복문 내부에서 continue 구문은 해당 루프(loop)를 건너뛰게 합니다.

# continue 라는 구문을 만나면, 반복문에서 continue 아래 작성된 코드는 실행되지 않고 건너뜁니다.

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 반복문과 조건문 그리고 continue를 활용하여 짝수만 출력해 주세요

# # 코드를 입력해 주세요
for i in mylist:

    if i % 2 == 1:
        continue
    print(i)

# [출력]
# 2
# 4
# 6
# 8
# 10

# break
# break 구문을 만나면, 반복 루프(loop)는 즉시 종료됩니다.

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# break를 사용하여 i가 6 이상이면 STOP

for i in mylist:
    if i >= 6:
        break
    print(i)
# [출력]


# 1
# 2
# 3
# 4
# 5

# break, continue 차이
for i in range(10):
    if i == 5:
        break
    print(i)
# [출력]

# 0
# 1
# 2
# 3
# 4
for i in range(10):
    if i == 5:
        continue
    print(i)
# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9


# While
# while 문은 while문과 함께 정의한 조건이 참이 동안 반복 루프를 수행합니다.

count = 5

while count > 0:
    print(count)
    count -= 1
# [출력]


# 5
# 4
# 3
# 2
# 1

# 많은 사용하는 방법 중 하나는 while True로 지정하여 무한 루프를 생성 후, 탈출 구문 루프 내에서 설정하는 것입니다.

count = 1

while True:
    print(count)
    count += 2
    # 탈출 구문(break)
    if count > 50:
        break
# [출력]

# 1
# 2
# 3
# 4
# 5

################################################################################################

# 연습문제

# 사용자의 입력이 'MALE', 'FEMALE'인 경우는 while 문을 종료하고, 그렇지 않으면 "잘못된 입력 값입니다."를 출력하세요

# input() 함수로 사용자로부터 입력을 받습니다.
# # 코드를 입력해 주세요
while True :
    sex = input('성별을 입력해주세요 : ')

    if sex == 'MALE' or sex == 'FEMALE':
        print('반복문 종료!!')
        break
    else :
        print('잘못된 입력 값입니다.')
# [출력]

# male
# 잘못된 입력 값입니다.
# animal
# 잘못된 입력 값입니다.
# FEMALE
# ====
# 프로그램 종료

# 연습 문제 2
# 1부터 50까지의 숫자 중에서 짝수의 합을 구하세요 (while 사용)

# # 코드를 입력해 주세요

count = 2
total = 0

while True:
    total += count

    print(f'count: {count}, total: {total}')

    count +=2

    if count > 50 :
        break

    
    
    
# [출력]

# count: 2, total: 2
# count: 4, total: 6
# count: 6, total: 12
# count: 8, total: 20
# count: 10, total: 30
# count: 12, total: 42
# count: 14, total: 56
# count: 16, total: 72
# count: 18, total: 90
# count: 20, total: 110
# count: 22, total: 132
# count: 24, total: 156
# count: 26, total: 182
# count: 28, total: 210
# count: 30, total: 240
# count: 32, total: 272
# count: 34, total: 306
# count: 36, total: 342
# count: 38, total: 380
# count: 40, total: 420
# count: 42, total: 462
# count: 44, total: 506
# count: 46, total: 552
# count: 48, total: 600
# count: 50, total: 650


# 연습 문제 3

# while을 이용하여 다음과 같이 @ 찍기에 도전해 보세요!

# # 코드를 입력해 주세요
count = 1

while True:
    
    print('@' * count)
    count += 1
    if count > 5 :
        break

# [출력]

# @
# @@
# @@@
# @@@@
# @@@@@
# # 코드를 입력해 주세요
num = 1
while num<=5:

    if num <=3:
        print('@' * num)
    else:
        print('@' * (6-num))
    num += 1
# [출력]

# @
# @@
# @@@
# @@
# @

from auto_commit import git_auto_push
git_auto_push('loops')