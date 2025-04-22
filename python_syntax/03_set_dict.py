#############################################################
#                                                           #
#                           SET                             #
#                                                           #
#############################################################

# 세트는 순서가 보장 되지 않습니다.

# 세트는 요소의 중복을 허용하지 않습니다.

# 세트는 {}를 활용하여 생성할 수 있습니다.

myset = set([1, 1, 1, 2, 2, 2, 3, 3, 3])

print(myset)

# Set에 값 추가 

myset.add('world')

myset.add(10)
myset.add(10)

print(myset)

# Set에 여러개 값 한번에 추가

myset.update([4,5,7])

print(myset)

myset.update((8,9,10))

print(myset)

myset.update({23,245,25})

print(myset)

# Set의 단일요소 제거

myset.remove('world')

print(myset)

# 교집합 (intersection)
# 교집합은 집합 A와 B가 주어졌을 때 공통된 요소를 말합니다.

# & 기호나 intersection() 메서드를 활용하여 교집합을 구할 수 있습니다.

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

a & b

test = a.intersection(b)

print(a & b)
print(test)

# 합집합 (union)
# 합집합은 집합 A와 B가 주어졌을 때 집합 A, B 요소 모두를 포함하는 것을 말합니다.

# |기호나 union() 메서드를 활용하여 합집합을 구할 수 있습니다.

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

union_test = a.union(b)

print(a | b)
print(union_test)

# 차집합 (difference)
# 두 집합에서, 하나의 집합에 포함되고 다른 집합에는 포함되지 않는 모든 원소의 집합.

# -연산자를 활용하거나 difference() 메서드를 활용하여 구할 수 있습니다.

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
# a 집합에서 b 집합을 뺀 차집합

print(a-b)


# 집합의 타입 변환
# set를 list로 변환

a = {1, 2, 3, 4, 5}

print(type(a))

b = list(a)

print(b)

dupli_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]

result2 = list(set(dupli_list))

print(result2)

conv_set = set(dupli_list)

result = list(conv_set)

print(result)

############################################################################################################################################################

# 연습문제 1
sample1 = {1, 2, 3, 4, 5}
sample2 = {2, 4, 5, 6, 7}

print(f'sample1: {sample1}')
print(f'sample2: {sample2}')
# sample1 에 6를 추가합니다.

# # 코드를 입력해 주세요
sample1.add(6)
# [출력]
print(f'sample1: {sample1}')
# {1, 2, 3, 4, 5, 6}


# sample2에 2를 제거합니다.

# # 코드를 입력해 주세요
sample2.remove(2)
# [출력]
print(f'sample2: {sample2}')
# {4, 5, 6, 7}


# sample1과 sample2의 교집합을 출력합니다.
# # 코드를 입력해 주세요
print(sample1 & sample2)

# [출력]
# {4, 5, 6}


# sample1과 sample2의 합집합을 출력합니다.
# # 코드를 입력해 주세요
print(sample1 | sample2)
# [출력]
# {1, 2, 3, 4, 5, 6, 7}


# sample1과 sample2의 차집합을 활용하여 다음과 같이 출력합니다.
# # 코드를 입력해 주세요

print(sample1 - sample2)
# [출력]
# {1, 2, 3}


# 연습문제 2
# 다음 리스트에서 중복된 항목을 제거하세요

# 최종 출력 값은 list 형태로 출력하세요

numList = [1, 3, 2, 3, 7, 6, 8, 4, 10, 5, 3, 8, 9]

# # 코드를 입력해 주세요
print(list(set(numList)))
# [출력]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#############################################################
#                                                           #
#                        DICTIONARY                         #
#                                                           #
#############################################################

# 순서를 가지지 않습니다.

# 키(key)와 값(value)의 쌍으로 이루어져 있습니다.

# type은 dict로 표시 됩니다.

# key를 사용하여 값을 조회할 수 있습니다.

# 딕셔너리는 수정, 삭제, 추가가 가능합니다.

mydict = dict()

print(type(mydict))

mydict = {'a': 1, 'b': 2, 'c': 3}

print(type(mydict))

# 딕셔너리는 여러 타입의 key를 가질 수 있습니다.

mydict = {'a': 1, '가':2, 100: 3, 3.14: 4, True: 5}

print(mydict)

# 값 조회
# key 값으로 값을 조회할 수 있습니다.

mydict = {'a': 1, '가':2, 100: 3, 3.14: 4, True: 5}

# key를 지정하여 값을 조회할 수 있습니다.

print(mydict['a'])
print(mydict[3.14])

# key가 없는 경우 Error가 발생합니다.

# print(mydict['b'])


# keys() : 모든 key 조회

mydict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

print(mydict.keys())

# dict_keys는 리스트(list)가 아닙니다.

# 객체(object)로 생성되는데, 이를 list로 변경하기 위해서는 list()로 타입 변환을 하면 됩니다.

print(type(mydict.keys())) # dict_keys라는 타입

print(list(mydict.keys()))

# values() : 모든 value 조회
print(mydict.values())

# dict_values([100, 200, 300, 400, 500])


# items() : 모든 key, value 조회
# key, value가 튜플로 묶여서 조회됩니다.

print(mydict.items())

# key 값의 존재 유무 확인

print('12' in mydict)


# 값을 추가하기
# 새로운 key에 값을 대입하여 추가


mydict = dict()

print(mydict)

mydict['apple'] = '12'

print(mydict)

# update() : 다중 업데이트
# 값을 한꺼번에 업데이트 합니다.

mydict = {'파인애플': 1500, '망고': 3500, '배': 1000}


fruit = {
    '사과': 2000, 
    '딸기': 3000, 
    '수박': 5000, 
}

mydict.update(fruit)

print(mydict)
print(fruit)


# 값 변경
# key 값에 새로운 값(value)를 대입하여 값을 변경할 수 있습니다.

mydict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

mydict['a'] = 'i am a'

print(mydict)


# 제거하기 / key 제거
mydict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

# pop() 에 key를 지정하여 값을 제거할 수 있습니다.

# 제거되는 값의 value를 반환합니다.

result = mydict.pop('c')

# [출력]

print(result)
print(mydict)

# len() : 요소의 개수 파악
print(len(mydict))


################################################################################################################################################

# 연습문제
# 학생들의 이름과 점수를 key와 value로 가지는 score 변수를 생성하세요.

# 하준 90점, 서윤 86점, 지아 80점

# # 코드를 입력해 주세요
stu_score = dict()

stu_score['하윤'] = 90
stu_score['서윤'] = 86
stu_score['지아'] = 80

print(stu_score)
# [출력]

# {'하준': 90, '서윤': 86, '지아': 80}

# score 변수에 수지 95점을 추가하세요.

# # 코드를 입력해 주세요
stu_score['수지'] = 95
print(stu_score)
# [출력]

# {'하준': 90, '서윤': 86, '지아': 80, '수지': 95}
# score 변수에서 지아를 삭제하세요.

# # 코드를 입력해 주세요
stu_score.pop('지아')

print(stu_score)
# [출력]

# {'하준': 90, '서윤': 86, '수지': 95}
# score 변수에 기창 98점, 남철 60점, 기성 75점을 한번에 추가하세요.

# update() 를 사용하세요
# # 코드를 입력해 주세요
stu_score.update({'기창': 98, '남철': 60, '기성': 75})

print(stu_score)
# [출력]

# {'하준': 90, '서윤': 86, '수지': 95, '기창': 98, '남철': 60, '기성': 75}

from auto_commit import git_auto_push
git_auto_push('Set && Dictionary')