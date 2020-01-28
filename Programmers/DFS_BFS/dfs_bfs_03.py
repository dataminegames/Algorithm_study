'''
# 문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
1. 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
2. 주어진 공항 수는 3개 이상 10,000개 이하입니다.
3. tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
4. 주어진 항공권은 모두 사용해야 합니다.
5. 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
6. 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''


def solution(tickets):
    r = []
    
    def dfs(curr, t):
        
        if not t:
            r.append(curr)
            
        for i, v in enumerate(t):
            if v[0] == curr[-1]:
                temp = t.copy()
                temp.pop(i)
                dfs(curr + [v[1]], temp)
    
    dfs(["ICN"], tickets.copy())
    
    return sorted(r, key=lambda x: "".join(x))[0]
    
    
solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']])
# ['ICN', 'JFK', 'HND', 'IAD']

solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']])
# ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']
