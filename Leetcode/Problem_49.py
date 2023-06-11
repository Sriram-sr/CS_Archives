strs = ["ac","c"]
addded_indexes = []
output = []

for word in range(len(strs)):
    if word not in addded_indexes:
        sub_list = []
        sub_list.append(strs[word])
        for nxt in range(word+1,len(strs)):
            if strs[nxt] == '' and sub_list[0] != '':
                break
            for char in strs[nxt]:
                if char not in strs[word]:
                    break
            else:
                if len(strs[nxt])==len(strs[word]):
                    sub_list.append(strs[nxt])
                    addded_indexes.append(nxt)
        output.append(sub_list)    

print(output)        
