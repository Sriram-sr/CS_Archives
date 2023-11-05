class Check :
    class_vari = 80
    
    def dummy(self):
        print("Instance created")

obj1 = Check()
obj1.class_vari = 100
print(Check.class_vari)
print(obj1.class_vari)
