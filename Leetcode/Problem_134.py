def can_complete_circuit(gas, cost):
    circle_flag = False
    circle_idx = -1
    for idx in range(len(gas)): # 3
        if gas[idx]<cost[idx]:
            pass
        else:
            circle = gas[idx:]+gas[:idx] #
            cost_circle = cost[idx:]+cost[:idx] 
            last_unit = circle[0]
            for unit in range(len(circle)): #0
                if unit==len(circle)-1:
                    last_unit = last_unit-cost_circle[unit]
                else:    
                    last_unit = last_unit-cost_circle[unit]
                    if last_unit<0:
                        break
                    last_unit+=circle[unit+1] 
            if last_unit>=0:
                circle_flag = True
                circle_idx = idx  
            
    return circle_idx

gas = [2,3,4]
cost = [3,4,3]
print(can_complete_circuit(gas,cost))

        
     
                   
            
