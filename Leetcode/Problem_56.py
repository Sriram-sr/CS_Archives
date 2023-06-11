intervals = [[1,4],[2,3]]
res_list = []
no_look_idxs = []
length = len(intervals)

if len(intervals) == 1:
    print(intervals)

for idx in range(length-1):
    if idx not in no_look_idxs:
        cmp_arr = intervals[idx+1]
        for val in cmp_arr:
            flag = 0
            for prev in intervals[idx]:
                print(val)
                if val<prev and val< intervals[idx][0]:
                    if intervals[idx+1][-1] > intervals[idx][-1]:
                        no_look_idxs.append(idx+1)
                        res_list.append([val,intervals[idx+1][-1]])
                        flag = 1
                        break
                    else:
                        no_look_idxs.append(idx+1)
                        res_list.append([val,intervals[idx][-1]])
                        flag = 1
                        break
                elif val<=prev:
                    no_look_idxs.append(idx+1)
                    res_list.append([intervals[idx][0],intervals[idx+1][-1]])
                    flag = 1
                    break
            if flag!=0:
                break    
        else:
            res_list.append(intervals[idx])
    if idx==length-2 and length-1 not in no_look_idxs:
        res_list.append(intervals[length-1])

print(res_list)