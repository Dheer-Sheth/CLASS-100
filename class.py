from unicodedata import name


class player(object):
    def __init__(self,name,age,weight,height,gender,goals):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.gender=gender
        self.goals= goals 

    def displayGoals(self,name,goals):
        print("name=",name)   
        print ("number of goals scored=",goals)  

lionel= player("lionel",34,"75 kilograms","5 feet 2 inches",'male',65)  
lionel.displayGoals("lionel",65)