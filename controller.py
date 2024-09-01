from product import Product
import csv
import controller as p

all_products = []
#Convert products to  csv
def convert_products_to_csv(listofproducts):
    file = open("products.CSV","w")
    file.write("")
    file.close()
    for p in listofproducts:
        f = open("products.CSV","a")
        f.write(f"{p.id},{p.name},{p.price},{p.qty}\n")
        f.close()   

#convert csv to product list
def convert_csv_to_product_list():
   all_products = []
   with open('products.CSV','r') as file:
      csv_reader = csv.reader(file)
      for row in csv_reader:
         p = Product(id=row[0], name=row[1], price=row[2], qty=row[3]) 
         all_products.append(p)
      return all_products


#Add product
def add_product():
   print("Adding product:")
   p = Product(id="", name="", price=0, qty=0) 
   p.id = int(input("Enter the id number of product: "))
   p.name = input("Enter the name of product: ")
   p.price = int(input("Enter the price  of product: "))
   p.qty = int(input("Enter the qty of product: "))
   f = open("products.CSV","a")
   f.write(f"{p.id},{p.name},{p.price},{p.qty}\n")
   f.close()
   print("the Product adding is successfull")

#view product
def view_product():
   print("view all product:")   
   f = open("products.CSV","r")
   print(f.read())

#view single product by id
def view_singleproduct():
      print("view single  product")
      id = input("Enter the product id:")
      all_products = []
      with open('products.csv','r') as file:
         csv_reader = csv.reader(file)
         for row in csv_reader:
            p = Product(id=row[0], name=row[1], price=row[2], qty=row[3]) 
            all_products.append(p)

      record_found = False
      product = Product(id="", name="", price=0, qty=0) 
      for p in all_products:
         if p.id == id:
            record_found = True
            product = p
            break
         else:
            record_found = False
      if record_found == True:
            print("record is found:")    
            product.product_display()
      else: print("product id is not found.")

#delect product
def delete_product():
    print(f"Deleting product")
    lists = p.convert_csv_to_product_list()
    print(lists)
    updated_product = []
    idtodelete = input("Enter product id: ")
    record_found = False
    for product in lists:
        if product.id == idtodelete:
            record_found = True
        else:
            updated_product.append(product)
    if record_found:
         p.convert_products_to_csv(updated_product)
         print("Deleted Successfully")
    else:
      print("No record found")

