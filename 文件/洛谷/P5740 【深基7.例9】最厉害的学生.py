num = int(input())
all_info = []
for _ in range(num):
    info = input().split()       
    info[1] = int(info[1])
    info[2] = int(info[2])
    info[3] = int(info[3])
    all_info.append(info)
maxinfo = ['']
if num == 1:
    maxinfo[0] = all_info[0]
else:
    for _ in range(num - 1):
        score1 = all_info[_][1] + all_info[_][2] + all_info[_][3]
        score2 = all_info[_ + 1][1] + all_info[_ + 1][2] + all_info[_ + 1][3]
        if score1 >= score2:
            all_info[_], all_info[_ + 1] = all_info[_ + 1], all_info[_]
            maxinfo[0] = all_info[_ + 1]
for i in range(4):
    print(str(maxinfo[0][i]), end=' ')
        

