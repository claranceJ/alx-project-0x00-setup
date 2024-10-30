class Fruits:
    #constructor
    def __init__(self,price,shape,name):
        self.price=price
        self.shape=shape
        self.name=name
    def display(self):
        print(f"My favourite fruit: {self.name} and its price: {self.price} with a shape of {self.shape}")


#create instance of a class.
my_Object=Fruits(20,"oval", "Banana")
my_Object.display()



