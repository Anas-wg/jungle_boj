# 정렬 조건
# 1. 길이가 짧은 것 부터
# 2. 길이가 같다면 사전 순
# 중복된 단어는 제거
import sys
input = sys.stdin.readline

N = int(input())
word_list = set([])

for i in range(N):
  word_list.add(input().rstrip())

word_list = list(word_list)
word_list.sort()
word_list.sort(key=lambda x : len(x))

for word in word_list:
    print(word)