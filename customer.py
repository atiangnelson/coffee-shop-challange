from order import Order
class Customer:
    def __init__(self,name):
        self.name = name
        

    def create_order(self,coffee,price):
        order=Order(self,coffee,price) 
        return order 


    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self,value):
        if  isinstance(value,str) and 1 <= len(value) <=15:
            self._name =value
        else:
            raise ValueError("Name must be a string") 
    @property
    def orders(self):
        return [order for order in Order.all_orders if order.customer==self ]        
    @property
    def coffees(self):
        return list({order.coffee for order in Order.all_orders if order.customer == self})