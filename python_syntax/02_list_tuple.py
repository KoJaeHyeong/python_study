from auto_commit import git_auto_push

movie = ['어벤져스', '아이언맨', '토르', '스파이더맨']

movie += ['엑스맨']

print(movie)

movie.insert(1, '데드풀')

print(movie)

movie.remove('아이언맨')

print(movie)

movie.pop(1)

print(movie)

kr_movie = ['승리호', '신세계', '타짜']

movie += kr_movie

print(movie)

# movie.sort()

sorted_movie = sorted(movie)

print(movie)

print(sorted_movie)

# indexing

mylist = ['P', 'Y', 'T', 'H', 'O', 'N']

print(mylist[1])

print(mylist[-2])

mylist[0] = 888

print(mylist)

mylist[-1] = 'Not N'

print(mylist)

mylist2 = [['가', '나', '다'], [4, 5, 6], 7, 8, 9]

print(mylist2[0])

print(mylist2[0][1])

mylist2[0][1] = 'Not 나'

print(mylist2)

# slicing

mylist3 = [100, 200, 300, 400, 500]

print(mylist3[3:])

print(mylist3[:2])

print(mylist3[1:3])

print(mylist3[::3])

print(mylist3[::-3])

# list 덧셈
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(a+b)

# list 곱셈
a = ['a', 'b', 'c']
b = [1, 2, 3, 4]

print(a * 2)
print(b * 3)


# 리스트와 튜플 연습문제


################### 인덱싱 && 슬라이싱 #########################


# list 인덱싱 & 슬라이싱을 사용하여 다음과 같이 출력 하세요
fruit = ['사과', '바나나', '파인애플', '배', '수박', '키위', '오렌지', '망고', '딸기']

print(fruit[2:5])

# [출력]
# ['파인애플', '배', '수박']

print(fruit[7:])
print(fruit[len(fruit)-2:])
# [출력]
# ['망고', '딸기']


# # 코드를 입력해 주세요
print(fruit[:3])
# [출력]
# ['사과', '바나나', '파인애플']

# # 코드를 입력해 주세요
print(fruit[3:])
# [출력]
# ['배', '수박', '키위', '오렌지', '망고', '딸기']


# 슬라이싱을 활용하여 짝수만 출력해 주세요

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 코드를 입력해 주세요
print(nums[1::2])

# [출력]
# [2, 4, 6, 8, 10]

# sample = [1, 2, 3, 4, 5, 6, 7, 8] 리스트를 슬라이싱을 이용하여 출력과 같이 나올수 있도록 코드를 채워주세요.

sample = [1, 2, 3, 4, 5, 6, 7, 8]
# 슬라이싱을 사용해 다음과 같이 출력해 주세요

# # 코드를 입력해 주세요
print(sample[:-1])
# [출력]
# [8, 7, 6, 5, 4, 3, 2, 1]

# 슬라이싱을 사용해 다음과 같이 출력해 주세요
# # 코드를 입력해 주세요
print(sample[2::2])
# [출력]
# [3, 5, 7]

# 슬라이싱을 사용해 다음과 같이 출력해 주세요
# # 코드를 입력해 주세요
print(sample[1::3])
# [출력]
# [2, 5, 8]

# 아래의 값을 저장하고 있는 myList 변수를 생성하세요.
# [[1,2,3],[4,5,6],[7,8]]


myList = [[1,2,3],[4,5,6],[7,8]]

# myList
# 9를 myList에 추가하여 아래의 값을 저장할 수 있도록 하세요.

# [[1,2,3],[4,5,6],[7,8,9]]
# # 코드를 입력해 주세요
myList[2].append(9)

print(myList)
# [출력]

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

from auto_commit import git_auto_push

git_auto_push("list && tuple")