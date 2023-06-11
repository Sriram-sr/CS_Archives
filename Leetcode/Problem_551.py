def give_attendance(record):
	if record.count('A')>=2:
		return False
	for idx in range(len(record)):
		if record[idx]=='L':
			if record[idx:idx+3].count('L')==3:
				return False
	return True

string = "PPALLAPL"	
print(give_attendance(string))				

	    	