class Base:
    def __init__(self,id,following):
        self.id=id
        self.following=following

    def display_followers(self):
        print(f"The user with id {self.id} has {self.following} followers")    

class Child(Base):
    def __init__(self,id,name,following,followers):        
        self.id=id
        self.name=name
        self.following=following
        self.followers=followers

        # Base.__init__(self,self.id,self.following)
        Base.__init__(self,id,following)

child1 = Child(1,'sriram',450,298)
child1.display_followers()

# basechild = Base(2,'Heroku')
# basechild.display_followers()