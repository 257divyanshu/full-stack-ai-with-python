# def process_order(item, quantity):
#     try:
#         price = {"masala": 20}[item]
#         cost = price * quantity
#         print(f"total cost is {cost}")
#     except KeyError:
#         print("Sorry that chai is not on menu")
#     except TypeError:
#         print("Quantity must be in number")
# 📍 NOTE : the TypeError exception is of no use here, because python supports string multiplication (or string repetition)

# 📍 failing fast version (making the TypeError exception block actually work)
# def process_order(item, quantity):
#     try:
#         if not isinstance (quantity, (int, float)):
#             raise TypeError('Quantity must be in number')
#         price = {"masala": 20}[item]
#         cost = price * quantity
#         print(f"total cost is {cost}")
#     except KeyError:
#         print("Sorry that chai is not on menu")
#     except TypeError as err:
#         print(err)        

# 📍 better version
def process_order(item, quantity):
    try:
        if not isinstance (quantity, (int, float)):
            print('Quantity must be in number')
            return
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")  
# 📍 EXPLANATION:
# - in larger Python projects, developers often skip the raise inside the function and just let the if statement print the error and return
# - this avoids the overhead of raising an exception if we plan to handle the mistake immediately anyway

process_order("ginger", 2)
process_order("masala", "two")