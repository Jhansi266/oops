# buy a cars using oops
class buying:
    def type(self,model):
        self.m=model
        print("car model",model)
    def colour(self,colo):
        self.c=colo
        print("colour",colo)
    def prize(self,cost):
        self.co=cost
        print("prize of car",cost)
    def display(self):
        print(self.m)
        print(self.c)
        print(self.co)
s=buying()
model=input("enter the model:")
s.type(model)
colo=input("enter the colour:")
s.colour(colo)
cost=int(input("enter the prize:"))
s.prize(cost)
s.display()

    

