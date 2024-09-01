class Product:
   def __init__(self,id,name,price,qty):
      self.id = id
      self.name = name
      self.price = price
      self.qty = qty

   def  product_display(self):
      print(f"product id is: {self.id}")
      print(f"product name is: {self.name}")
      print(f"product price is: {self.price}")
      print(f"product qty is: {self.qty}")



#p1 = Product(id="1", name="iphone", price="50000", qty=10) 
#p2 = Product(id="2", name="phone", price="5000", qty=1) 

