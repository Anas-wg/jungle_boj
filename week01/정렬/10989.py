import sys
input = sys.stdin.readline
from collections import defaultdict


def counting_sort(num_list):
    max_value = max(num_list)  # 입력된 숫자의 최대값을 찾음
    # count = [0] * (max_value + 1)  # 0부터 max_value까지 저장할 배열 생성 => 메모리 초과 원인
    count = defaultdict(int)  # 기본값이 0인 딕셔너리 생성
    
    # 각 숫자의 등장 횟수를 저장
    for num in num_list:
        count[num] += 1

    #정렬된 결과를 생성
    sorted_list = []
    for i in range(len(count)):
        sorted_list.extend([i] * count[i])  # 해당 숫자를 등장 횟수만큼 추가

    return sorted_list

N = int(input())  # 입력 개수
num_list = [int(input()) for _ in range(N)]  # 입력 리스트 생성


result = counting_sort(num_list)


print("\n".join(map(str, result)) + "\n")



import sys 
N = int(sys.stdin.readline().rstrip())
cnt_dic = {}
for _ in range(N):
    X =int(sys.stdin.readline().rstrip())   
    if X in cnt_dic: # X가 dic의 키에 없다면 
        cnt_dic[X] += 1
    else:
        cnt_dic[X] = 1
for i in range(max(cnt_dic.keys())+1):
    if i not in cnt_dic:
        continue
    else:
        for _ in range(cnt_dic[i]):
            print(i)