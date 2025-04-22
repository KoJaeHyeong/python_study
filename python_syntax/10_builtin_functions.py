# 10. 내장함수(Built-in Function)

# 파이썬에는 이미 만들어진 내장함수(built-in function)가 존재합니다.

# 이미 사용하고 있는 print(), type()이 파이썬의 대표적인 내장함수입니다.

# 이 밖에도 유용한 몇 가지 내장함수를 알아 보겠습니다.

# map
# 문법: map(function, iterable)

# map은 함수(f)와 순회 가능한(iterable) 자료형을 입력으로 받습니다.

# map은 입력받은 자료형의 각 요소를 함수(function)가 수행한 결과를 묶어서 돌려줍니다.

sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# map만 실행시 요소의 내용이 바로 출력되지 않습니다.

map(str, sample_data)
# [출력]

# list()로 타입 변환하여 요소를 출력합니다.
print(list(map(str, sample_data)))
print(type(map(str, sample_data)))

# [출력]
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# map에 lambda 함수 적용
result = map(lambda x: x*2, sample_data)

print(list(result))
# [출력]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# map에 다중 인수를 지정
sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_data_2 = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = list(map(lambda x, y: x+y, sample_data, sample_data_2))
print(result)
# [출력]
# [1, 3, 5, 7, 10, 14, 20, 29, 43, 65]


# list의 size가 다른 경우, 작은 size에 맞춰 생성
sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_data_2 = [1, 1, 1, 10, 100]
result = list(map(lambda x, y: x+y, sample_data, sample_data_2))
print(result)
# [출력]
# [2, 3, 4, 14, 105]


# zip
# 문법: zip(*iterable)

# 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 합니다. (튜플의 형태로)

sample_data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_data2 = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55]
sample_data3 = [5, 6, 7]

# sample_data1, sample_data2을 zip으로 묶어준 경우

result = zip(sample_data1, sample_data2)
print(list(result))
# [출력]
# [(1, 0),
#  (2, 1),
#  (3, 2),
#  (4, 3),
#  (5, 5),
#  (6, 8),
#  (7, 13),
#  (8, 21),
#  (9, 34),
#  (10, 55)]

# sample_data1, sample_data2, sample_data3을 zip으로 묶어준 경우

# 작은 size를 가지는 리스트(list)에 맞춰 생성합니다.
result = list(zip(sample_data1, sample_data2, sample_data3))
print(result)
# [출력]
# [(1, 0, 5), (2, 1, 6), (3, 2, 7)]

# zip의 응용

number = [1, 2, 3, 4]
name = ['홍길동','김철수','John','Paul']
number_name = list(zip(number,name))
print(number_name)

# [출력]
# [(1, '홍길동'), (2, '김철수'), (3, 'John'), (4, 'Paul')]

# zip을 활용한 dict 만들기
number = [1, 2, 3, 4]
name = ['홍길동','김철수','John','Paul']

dic = {}

for number, name in zip(number,name): 
    dic[number] = name

print(dic)
# [출력]
# {1: '홍길동', 2: '김철수', 3: 'John', 4: 'Paul'}



# enumerate (순서가 있는 자료형)
# [문법]: enumerate(iterable, start=0)

# 순서가 있는 자료형을 입력 받아 index를 포함하는 객체로 return 합니다.

# 일반 range() 함수를 사용한 경우

for value in range(1, 10, 2):
    print(value)
# [출력]
# 1
# 3
# 5
# 7
# 9

# enumerate() 함수를 사용하여 index를 return 받은 경우 (index를 정할 수 있다...?)

for idx, value in enumerate(range(1, 10, 2)):
    print(f'index: {idx}, value: {value}')
# [출력]
# index: 0, value: 1
# index: 1, value: 3
# index: 2, value: 5
# index: 3, value: 7
# index: 4, value: 9

############################################################################################################

# 연습문제
# map()을 활용하여 sample 리스트 요소의 제곱을 리스트 형식으로 출력하세요

sample = [2, 4, 6, 8, 10]
# # 코드를 입력해 주세요
result = list(map(lambda x: x**2, sample))
print(result)
# [출력]
# [4, 16, 36, 64, 100]

# zip()과 반복문을 활용하여 다음과 같이 출력해 주세요

fruit = ['사과', '자두', '딸기', '망고']
price = [1000, 3000, 2500, 6000]

# 코드를 입력해 주세요
for a, b in zip(fruit,price):
     print(f'({a} / {b} 원) ')
    
# [출력]
# (사과 / 1000 원)

# (자두 / 3000 원)

# (딸기 / 2500 원)

# (망고 / 6000 원)


from auto_commit import git_auto_push
git_auto_push('builtin_functions')