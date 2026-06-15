def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    print("starting the while loop")
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala Chai")
stall.send("Ginger Chai")
stall.send("Plain Chai")