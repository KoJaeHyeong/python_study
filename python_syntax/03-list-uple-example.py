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


# 함수 호출 예시
git_auto_push("오늘의 변경사항 커밋")