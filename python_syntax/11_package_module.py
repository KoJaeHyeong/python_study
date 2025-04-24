# 11. 패키지(Package)와 모듈(Module)

# 패키지와 모듈의 관계
# 함수들이 뭉쳐진 하나의 .py 파일 안에 이루어진 것을 모듈이라고 합니다.

# 여러 개의 모듈을 그룹화 하면 패키지가 됩니다.

# 패키지는 종종 라이브러리라고도 불리웁니다.

# from IPython.display import Image
# # 출처: pythonstudy.xyz
# Image('http://pythonstudy.xyz/images/basics/python-package.png')


# 즉, 하나의 .py 파일은 모듈이며, 모듈을 포함하는 디렉토리(directory)는 패키지로 정의됩니다.

# 모듈 import

# 모듈 import는 외장 라이브러리의 모듈을 불러오는 유용한 기능입니다.

# 모듈 import를 통해 는 다른 누군가가 이미 만들어 놓은 기능을 쉽게 가져와 사용할 수 있습니다.

# 파이썬 모듈을 가져와 사용하기 위해서는 import 구문을 사용합니다.

# 파이썬 모듈을 import 하는 방법은 여러가지 방식이 존재합니다.

# random 모듈 import

import random
a = [1, 2, 3, 4, 5]

# # random 모듈의 shuffle 함수를 실행
random.shuffle(a)

print(a)
# [출력]

# [1, 5, 4, 2, 3]
# random모듈을 rd 별칭(alias) 지정

import random as rd
b = [1, 2, 3, 4, 5]

# # rd 별칭으로 지정한 random 모듈의 shuffle 함수를 실행
rd.shuffle(b)
print(b)
# [출력]

# [2, 1, 3, 5, 4]
# random 모듈의 shuffle() 함수 import

from random import shuffle
c = [1, 2, 3, 4, 5]

# # import한 shuffle 함수를 실행
shuffle(c)
print(c)
# [출력]


# [1, 4, 3, 2, 5]
# 자주 사용하는 파이썬 데이터 분석 모듈
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import random

# numpy: 과학 계산을 위한 패키지

# pandas: 데이터 분석을 할 때 가장 많이 쓰이는 모듈

# matplotlib: 시각화를 위한 모듈

# seaborn: 시각화를 위한 모듈 (matplotlib을 더 쉽게 사용할 수 있도록 도와주는 패키지)

# random: 난수 생성 관련 모듈

# # 0.0에서부터 1.0 사이의 실수(float) 난수 생성
print(random.random())
# [출력]

# 0.4584813159921739

# # shuffle
a = [1, 2, 3, 4]
random.shuffle(a)
print(a)
# [출력]
# [3, 4, 2, 1]

# # start포함 end미만 사이에서 랜덤한 정수 난수 생성
print(random.randrange(3, 10))
# [출력]


# 7

from auto_commit import git_auto_push
git_auto_push('package_module')