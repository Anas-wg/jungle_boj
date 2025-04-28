string_A = 'ABCDEF'
string_B = 'GBCDFE'

def LCSubstring(str_1, str_2):
    m, n = len(str_1), len(str_2)
    # 2차원 배열 초기화
    LCS = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0  # 길이 저장용 변수
    end_idx = 0  # 문자열 찾기 위한 인덱스 저장 변수

    for i in range(1, m + 1): 
        for j in range(1, n + 1):
            # 두 문자열을 한글자씩 비교
            if str_1[i - 1] == str_2[j - 1]:
                # 같다면 i - 1, j - 1 에 1 더함
                LCS[i][j] = LCS[i - 1][j - 1] + 1
                if LCS[i][j] > max_len:
                    max_len = LCS[i][j]
                    end_idx = i  # Optional: to retrieve substring
            else:
                LCS[i][j] = 0

    # Optional: to get the substring itself
    substring = str_1[end_idx - max_len:end_idx]
    return max_len, substring

def LCS_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    LCS = [[0]*(n+1) for _ in range(m+1)] # 마지막 [M][N]에 LCS 길이가 저장

    # LCS 배열 채우기
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]: # 같다면 그 이전 LCS에 마지막 글자 붙이기(길이 +1 증가)
                LCS[i][j] = LCS[i-1][j-1] + 1
            else: # 다르면 둘다 버려보고 더 긴거로 진행
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    
    # 백트래킹으로 문자열 추적
    i, j = m, n
    lcs = []

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])  # 현재 문자가 LCS의 일부
            # 대각선위로 이동
            i -= 1
            j -= 1
        elif LCS[i-1][j] >= LCS[i][j-1]:
            i -= 1  # 위쪽으로 이동
        else:
            j -= 1  # 왼쪽으로 이동

    return LCS[m][n], ''.join(reversed(lcs))   # 최종 LCS 길이, 문자열


