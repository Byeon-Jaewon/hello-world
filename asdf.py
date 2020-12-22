def solution(n, t1, t2):
    lst=[]
    team=[]
    for i in range(1,n+1) :
        if i not in t1 :
            if i not in t2 :
                lst.append(i)
    for i in range(0, len(t1)):
        team.append(sorted([t1[i], t2[i]]))
    for i in range(0, len(team)) : 
        if team[i][0] in team[i+1] or team[i][1] in team[i+1] :
            s\\
    
    

        

    
    print(lst)
    print(team)
    answer = sorted(lst)
    return answer

solution(10, [9, 4, 4, 4, 7], [2, 10, 7, 6, 3])