# movie = ["spy", "spy", "spy", "ray", "ray", "once", "once", "room"]
#
#
# def solution(movie):
#     sets = set(movie)
#     movies = {}
#     for s in sets:
#         movies[s] = 0
#     for m in movie:
#         movies[m] += 1
#     temp = []
#     for movie in movies:
#         temp.append((movie, movies[movie]))
#     temp.sort(key=lambda x: (-x[1], x[0]))
#     answer = []
#     for t in temp:
#         answer.append(t[0])
#     return answer
#
#
# solution(movie)
#practice