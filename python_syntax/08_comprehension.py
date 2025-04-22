# 08. 컴프리헨션(Comprehension)

# 컴프리헨션(Comprehension)은 파이썬의 자료구조에 데이터를 좀 더 효율적이고 간결하게 표현하기 위한 문법입니다. 컴프리헨션 문법은 다음과 같은 특징을 가집니다.

# 파이썬 고유의 아름다운 문법

# 반복문(for ~ in)과 조건문 그리고 변수에 대한 연산까지 모두 갖춘 편리한 문법입니다.

# comprehension의 종류로는 list, set, dict등이 존재합니다.

# [실제 사례 연구]

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 이라는 list를 만들어 주고 우리는 이 중 짝수만 출력하고 싶을때는 어떻게 했었을까요?

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in mylist:
#     # 짝수 출력을 위한 조건문 생성
#     if i % 2 == 0:
#         print(i)
# [출력]

# 2
# 4
# 6
# 8
# 10

# 그럼 mylist 이라는 list에서 짝수만 따로 list로 만들어 주고 싶을 때는 어떻게 할까요?

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 짝수를 만들이 위한 빈 리스트 생성
# even = []

# for i in mylist:
#     if i % 2 == 0:
#         # even 리스트에 값 추가
#         even.append(i)

# print(even)
# [출력]


# [2, 4, 6, 8, 10]
# 이렇게 for in 문으로 해줄 수 있습니다. 하지만, comprehension 문법을 사용하면 쉽고 간결한 코딩이 가능합니다.

# comprehension 예시
# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 아래 문법이 바로 list comprehension 입니다. 한 줄로 해결해 버리는 것이 매력이에요

even = [i for i in mylist if i % 2 == 0]
print(even)
# [출력]

# [2, 4, 6, 8, 10]
# STEP 1: 반복문 생성
# even = [for i in mylist]
# 반복문 안에서 변수를 맨 앞에 한 번더 선언해 주지 않는다면 당연히 에러가 나게 됩니다.

# for i in mylist 구문에서 반복문을 돌면서 i 값이 return 된다고 생각하고 그 변수를 list에 다시 넣어주는 원리입니다.

# 즉, i를 for 문 맨 앞에 써주세요

even = [i for i in mylist]
print(even)
# [출력]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# STEP 2: 조건 필터 추가
# 조건문은 for ~ in 구문 맨 뒤에 추가하도록 합니다.

# [i for i in mylist (이곳에 조건문)]

print([i for i in mylist if i % 2 == 0])
# [출력]


# [2, 4, 6, 8, 10]

# 자, 이제 mylist의 요소 중 짝수만 추출하여 리스트(list)로 만들어 주는 list comprehension이 완성되었습니다.

# STEP 3: 변수 값에 별도의 연산 추가

# STEP 2 까지 완성된 짝수만 담는 list comprehension을 그대로 가져옵니다.

even = [i for i in mylist if i % 2 == 0]
# even
# [출력]

# [2, 4, 6, 8, 10]
# even 변수에는 현재 [2, 4, 6, 8, 10] 요소가 존재합니다.

# 모든 값에 제곱 를 해보도록 하겠습니다.

# i 변수에 제곱 연산을 추가합니다.
even = [i**2 for i in mylist if i % 2 == 0]
print(even)
# [출력]

# [4, 16, 36, 64, 100]

# Set Comprehension
# set comprehension은 comprehension 문법을 세트(set)로 생성합니다.

# 괄호를 {}로 생성하면 set comprehension이 완성됩니다.

set_even = {i**2 for i in mylist if i % 2 == 0}
print(set_even)
# [출력]

# {4, 16, 36, 64, 100}

# Dict Comprehension
# dict comprehension은 comprehension 문법을 활용하여 딕셔너리(dictionary)를 생성합니다.


# 괄호는 {}로 생성하고, key:value 형식을 반드시 지정합니다.

dict_even = {i:i**2 for i in mylist if i % 2 == 0}
print(dict_even)
# [출력]

# {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

from auto_commit import git_auto_push
git_auto_push('comprehension')