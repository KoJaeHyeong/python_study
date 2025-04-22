# 09. 함수(Function)

# 파이썬에서 함수는 자주 사용되는 코드 및 반복되는 코드를 모아 하나의 기능으로 만들고 이름을 붙인 것입니다. 변수를 이용해서 데이터에 이름을 붙여주는 것처럼, 함수를 이용해 프로그램 코드에 이름을 붙일 수 있습니다.

# 이렇게 이름을 붙여두면 이름을 통해 필요한 대상을 호출할 수 있습니다. 즉 함수의 이름을 불러 함수 내용으로 정의된 프로그램을 실행시킬 수 있는 것입니다.

# 따라서, 함수의 가장 중요한 기능은 바로 코드의 재사용성이 됩니다.

# 함수의 기본 구조
# def 키워드로 시작합니다.

# 함수명을 기입합니다.

# () 안에 매개변수를 지정할 수 있고, 생략도 가능합니다.

# 끝에는 :으로 끝납니다.

# 함수의 범위 안에서는 들여쓰기를 합니다. 들여쓰기가 끝난 지점이 함수의 범위가 끝나는 지점입니다.

# (예시)

def add_function(a, b):
    result = a + b
    return result
# 함수의 다양한 형태
# 일반 형태
# 입력 매개변수: O
result = add_function(0, 1)
print(result)

# return: O

def sample_function(a, b):
    result = a + b
    return result

# 입력 매개변수가 없는 형태

def sample_function():
    a = 1
    b = 2
    result = a + b
    return result

# return 이 없는 형태
def sample_function(a, b):
    result = a + b
    print(f'result: {result}')

# 입력 매개변수, return 모두 없는 형태
def sample_function():
    print('Hello, World!')

# 함수의 이름 및 호출
# 함수의 이름은 알파벳이나 _로 시작해야 합니다.

# 함수의 지정된 이름과 () 로 호출 할 수 있습니다.

def sample_function():
    print('함수가 호출 되었습니다!')

# 함수의 이름만 출력시

print(sample_function)
# [출력]


# 호출(call): 함수의 이름과 함께 ()를 같이 실행

sample_function()
# [출력]
# 함수가 호출 되었습니다!

# 함수의 이름을 별도의 변수에 대입한 후 변수에 ()를 같이 실행한 경우

a = sample_function
a()
# [출력]
# 함수가 호출 되었습니다!

# return 이 존재하는 경우
def sample_function():
    print('함수가 호출 되었습니다!@@@@')
    return 123

# return 값이 존재하는 경우 함수는 결과 값을 반환 하며 반환된 결과를 변수에 대입할 수 있습니다.

result = sample_function()

print(result)
# [출력]
# 함수가 호출 되었습니다!
# result
# [출력]

# 123
# 하지만, 함수가 아무런 결과 값을 반환하지 않는다면 함수로부터 반환된 결과는 None입니다.

# # return 이 없는 경우
def sample_function():
    print('함수가 호출 되었습니다!')

result = sample_function()
 
# [출력]
# 함수가 호출 되었습니다!
print(result)
# [출력]
# None

# docstring
# 함수에 대한 설명을 기록
def sample_function():
    """
    함수에 대한 설명을 기록합니다.
    sample_function은 함수를 설명하기 위한 예제 함수 입니다.

    (예시)
    호출의 예.
    sample_function()
    """
    print('함수가 호출 되었습니다.')

sample_function()
# [출력]

# 함수가 호출 되었습니다.

# 함수명.__doc__로 docstring을 출력할 수 있습니다.

print(sample_function.__doc__)

###############################################################################################################

# 1) 함수의 인수(매개변수)

# [참고]

# 인수(argument): 값, 변수, 참조 등 전달되는 값

# 매개변수(parameter): 함수 등에서 사용되는 전달된 값을 받는 변수

# 10, 20 이라는 값은 인수(argument)

# a, b는 매개변수(parameter)

def some_function(a, b):
    result = a + b
    return result

result = some_function(10, 20)
print(result)
# [출력]
# 30

# 위치 인수(positional arguments)
# 가장 보편적인 인수입니다.

# 변수명을 인수로 지정합니다.

# 위치가 중요합니다.

# a, b, c를 위치인수로 지정한 경우

def add_function(a, b, c):
    result = a + b + c
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'sum: {result}')
    return result

print(add_function(1, 3, 5))
# [출력]
# a: 1, b: 3, c: 5
# sum: 9
# 9

# 키워드 인수(keyword arguments)
# 위치 인수의 위치를 정확히 기억 하지 못하고 혼란을 야기할 수 있기 때문에 인수명에 값을 직접 지정합니다.

def add_function(a, b, c):
    result = a + b + c
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'sum: {result}')
    return result
# 아래의 예제는 키워드로 매개변수에 대한 값을 지정하는 예시입니다.

print(add_function(b=2, c=1, a=2))
# [출력]
# a: 5, b: 3, c: 1
# sum: 9
# 9


# 기본 매개변수(default parameter)
# 매개변수에 기본 값을 지정할 수 있습니다.

# 기본 값을 지정시 인수에 값을 생략 가능합니다.

# 단, 기본 값이 지정된 인수는 위치 인수보다 다음에 위치해야 합니다.

def add_function(a, b=0, c=0):
    result = a + b + c
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'sum: {result}')
    return result

print(add_function(1))
# [출력]
# a: 1, b: 0, c: 0
# sum: 1
# 1

add_function(1, 3)
# [출력]
# a: 1, b: 3, c: 0
# sum: 4
# 4

add_function(1, 3, 5)
# [출력]
# a: 1, b: 3, c: 5
# sum: 9
# 9

add_function(c=5, b=3, a=1)
# [출력]
# a: 1, b: 3, c: 5
# sum: 9
# 9

# 기본 매개변수가 위치 인수보다 앞 쪽에 위치한 경우 Error가 발생합니다.

# def add_function(a=0, b, c):
#     result = a + b + c
#     print(f'a: {a}, b: {b}, c: {c}')
#     print(f'sum: {result}')
#     return result


# *tuple (가변 매개변수)

# 여러 개의 인수를 전달 받을 수 있습니다.

# 여러 개의 인수를 전달 받은 *args에는 튜플(tuple) 형식으로 데이터가 저장됩니다.

# *args로 받은 인수는 반복문으로 처리하는 것이 일반 적입니다.

# 대체적으로 *args 변수가 많이 사용됩니다.

def add_function(*args):
    result = 0
    print(f'args의 타입: {args}')
    print(f'args의 타입: {type(args)}')
    for arg in args:
        print(arg)
        result += arg
    print('==='* 5)
    print(f'sum: {result}')

# 아무런 값을 전달하지 않은 경우(생략 가능)

add_function()
# [출력]
# args의 타입: 
# ===============
# sum: 0

# 1개의 값을 전달한 경우

add_function(1)
# [출력]
# args의 타입: 
# 1
# ===============
# sum: 1
# 복수의 값을 전달한 경우

add_function(1, 2, 3, 4, 5)
# [출력]
# args의 타입: 
# 1
# 2
# 3
# 4
# 5
# ===============
# sum: 15


# 위치 매개변수와 *tuple 매개변수의 혼용
# *tuple 매개변수는 위치 매개변수의 뒤에 위치해야 합니다.

def add_function(a, *args):
    print(f'a: {a}')
    print('==='* 5)
    result = 0
    for arg in args:
        print(arg)
        result += arg
    print('==='* 5)
    print(f'sum: {result}')

# 아무런 값을 지정하지 않은 경우

# 위치 매개변수 미지정으로 인한 Error 발생
# add_function()
# 단일 값을 지정한 경우

add_function(1)
# [출력]

# a: 1
# ===============
# ===============
# sum: 0


# 복수의 값을 지정한 경우
add_function(1, 2, 3, 4, 5)
# [출력]
# a: 1
# ===============
# 2
# 3
# 4
# 5
# ===============
# sum: 14


# **dict 인수 (키워드 가변 매개변수)
# 여러 개의 인수를 전달 받을 수 있습니다.

# 여러 개의 인수를 전달 받은 **kwargs에는 딕셔너리(dict) 형식으로 데이터가 저장됩니다.

# **kwargs로 받은 인수 역시 반복문으로 처리하는 것이 일반 적입니다.

# 대체적으로 **kwargs 변수가 많이 사용됩니다.

def add_function(**kwargs):
    print(type(kwargs))
    total_age = 0
    for name, age in kwargs.items():
        print(f'이름: {name}, 나이: {age}')
        total_age += age
    print('==='* 5)
    print(f'전체 나이의 합계: {total_age}')
# 아무런 값을 지정하지 않은 경우

add_function()
# [출력]

# ===============
# 전체 나이의 합계: 0
# 단일 값을 지정한 경우

add_function(lee=5)
# [출력]


# 이름: lee, 나이: 5
# ===============
# 전체 나이의 합계: 5

add_function(john=10, peter=12, lee=5)
# [출력]
# 이름: john, 나이: 10
# 이름: peter, 나이: 12
# 이름: lee, 나이: 5
# ===============

# 전체 나이의 합계: 27
# 딕셔너리(dictionary)를 인수로 지정하는 경우 **를 앞에 붙혀 줍니다.

person = {'john': 10, 'peter': 12, 'lee': 5}
print(person)
# [출력]
# {'john': 10, 'peter': 12, 'lee': 5}

add_function(**person)
# [출력]
# 이름: john, 나이: 10
# 이름: peter, 나이: 12
# 이름: lee, 나이: 5
# ===============
# 전체 나이의 합계: 27

################################################################################################

# 연습문제
# 가변 매개변수를 활용한 함수를 생성하여 요소의 개수를 구하고 출력하는 프로그램을 만들어 주세요

# Tip)
# 코드를 입력해 주세요
def count_function(*args):
    print(f'전달한 요소의 개수는: {len(args)} 개 입니다.')

# 검증코드
count_function()
# [출력]\
# 전달한 요소의 개수는: 0 개 입니다.

# # 검증코드
count_function(1, 2, 3)
# [출력]
# 전달한 요소의 개수는: 3 개 입니다.

# # 검증코드
count_function(1, 2, 3, 4, 5)
# [출력]
# 전달한 요소의 개수는: 5 개 입니다.


################################################################################################

# 2) Lambda : 익명 함수(Annonymous Function)

# 이름 없이 정의된 함수 입니다.

# 단일 문장(1줄)의 코드로 작성되어야 합니다.

# 함수 내부에서는 return문이 포함하지 않지만 값을 반환합니다.

# 단일 인수를 가지는 lambda 함수

a = lambda x: x * 2
print(a(4))
# [출력]
# 8


# 2개의 인수를 가지는 lambda 함수

a = lambda x, y: x * y
print(a(4, 8))
# [출력]
# 32

# 기본 값이 지정된 인수를 가지는 lambda 함수

a = lambda x, y=10: x * y
print(a(3))
# [출력]
# 30

# 키워드 인수를 지정하는 lambda 함수
print(a(y=5, x=3))
# [출력]
# 15

# lambda 함수 내부에서 조건문 사용

a = lambda x, y: x * y if x > 0 else y
print(a(4, 8))
# [출력]
# 32

print(a(-1, 8))
# [출력]
# 8

# 다음과 같이 elif 구문을 억지로 생성할 수 있습니다.

# 하지만, 복잡한 조건문을 사용하기 위해서는 일반적인 함수 사용을 권장합니다. (코드의 가독성이 떨어집니다.)

a = lambda x: x * 10 if x < 2 else (x**2 if x < 4 else x + 10)
print(a(1))
# [출력]
# 10

print(a(3))
# [출력]
# 9

print(a(4))
# [출력]
# 14

############################################################################################################

# 연습문제

# 연습문제 1
# 알파벳 문자열을 인수로 넣으면 함수를 구현하세요

# 함수의 이름은 capital_letter 로 선언합니다.

# 함수는 letter라는 위치인수를 가집니다.

# 함수는 letter인수에 받은 문자열을 모두 대문자로 바꾸고, 바꾼 값을 return 합니다.

# # 코드를 입력해 주세요

def capital_letter(letter: str) :
    return letter.upper()

result = capital_letter("My Name is Elsa")
print(result)
# [출력]
# 'MY NAME IS ELSA'

# 연습문제 2
# def calc_many(choice, *args) 함수에서

# choice가 sum 이면 합을 구해서 return 합니다.

# choice 가 mul 이면 곱한 결과를 return 합니다.

# 함수를 구현하세요

# # 코드를 입력해 주세요
def calc_many(choice='sum' or 'mul', *args):
    
    result = 1
    
    for i in args:
        if choice == 'sum' :
            result += i
        if choice == 'mul' :
            result *= i

    return result -1 if choice == 'sum' else result
        
print(calc_many('sum', 0, 1, 2, 3, 4))    
# # 결과: 10
print(calc_many('mul', 1, 2, 3, 4, 5))
# # 결과: 120

from auto_commit import git_auto_push
git_auto_push('functions')