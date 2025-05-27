from customer import Customer
from order import Order



class Coffee:
    def __init__(self,name):
        if isinstance(name,str) and len(name) >=3:
          self._name=name
        else:
           raise ValueError("Name must be string with atleast three characters")  
        

    @property
    def name(self):
       return self._name

    @name.setter
    def name(self,value):
       raise AttributeError("Name cannot be changed upon initialization")    
    
    @property
    def orders(self):
       return[order for order in Order.all_orders if order. coffee==self]
    
    @property
    def customers(self):
       return list({order.customer for order in Order.all_orders if order.coffee == self})
    @property
    def num_orders(self):
       return len([order for order in Order.all_orders if order.coffee == self])
    @property
    def average_price(self):
       if not self.orders:
          return 0
       return sum(order.price for order in self.orders)/len(self.orders)