let test_list = ['Gfg', 'is', 'best', 'for', 'Geeks'];

for(let sub=0;sub<test_list.length;sub++){
        let len = test_list[sub].length;
	for(let char=0;char<len;char++){
		if (test_list[sub][char] === 'G'){
			let sub_str = test_list[sub];
			let new_str = sub_str.replace('G','e')
			test_list[sub] = new_str;
			console.log(test_list);
		}
		if (test_list[sub][char] === 'e'){
			let sub_str = test_list[sub];
			let new_str = sub_str.replace('e', 'G');
			test_list[sub] = new_str;
		}
	}
}

console.log(test_list);
