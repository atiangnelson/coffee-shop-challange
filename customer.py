



class Customer:
    def __init__(self,name):
        self.name = name


    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self,value):
        if  isinstance(value,str) and 1 <= len(value) <=15:
            self._name =value
        else:
            raise ValueError("Name must be a string") 

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer==self ]        
    
    def coffees(self):
        from order import Order
        return list({order.coffee for order in Order.all_orders if order.coffee == self})