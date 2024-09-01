import controller as p

option_text = """
Enter the  number (1 to 4) according to your choice.
1:add product
2:view all product
3:view single product 
4:delete product
"""
option = int(input(option_text))
if option == 1:
    p.add_product()
elif option == 2:
    p.view_product()
elif option == 3:
    print("view single  product by Id")
    p.view_singleproduct()
elif option == 4:
    print("delete product")  
    p.delete_product()  

else:
   print("please Enter the number 1 to 4 ")   