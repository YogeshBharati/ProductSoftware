import csv
from product import Product
def convert_csv_to_product_list():
   all_products = []
   with open('products.CSV','r') as file:
      csv_reader = csv.reader(file)
      for row in csv_reader:
         p = Product(id=row[0], name=row[1], price=row[2], qty=row[3]) 
         all_products.append(p)
         return all_products
all_prod = convert_csv_to_product_list()
print(all_prod)


