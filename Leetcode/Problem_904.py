def total_fruits(fruits):
	all_fruit_collection = []
	for idx in range(len(fruits)):
		temp_list = []
		for fruit in range(idx,len(fruits)):
			temp_list.append(fruits[fruit])
			if len(set(temp_list))==3:
				temp_list = temp_list[:-1]
				break

		all_fruit_collection.append(temp_list)	
		
	return len(max(all_fruit_collection, key=len))
		    	

# this above solution failed as time exceeded. below is efficient one
def totalFruit(fr: list[int]) -> int:
        
    l = i = 0                            # [1] left and intermediate indices
    m = 0                                # [2] max interval length
    bs = [-1,-1]                         # [3] fruit counts in the basket
    
    for r in range(len(fr)):             # [4] move right end
        if fr[r] != bs[1]:               # [5] when encountered a different fruit
            if fr[r] != bs[0]: l = i     #     - update left end for the new earliest type
            i = r                        #     - update index of the first entrance of this type
            bs[0], bs[1] = bs[1], fr[r]  #     - update earliest/latest pair in the basket
        m = max(m, r - l + 1)  

    return m

fruits = [0,1,2]
# print(total_fruits(fruits))
print(totalFruit(fruits))