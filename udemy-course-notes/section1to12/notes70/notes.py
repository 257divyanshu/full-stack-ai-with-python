import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)
        
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")

# 📍 OUTPUT
# 0s Taking order for #1
# 0s Brewing chai for #1
# 2s Taking order for #2
# 3s Brewing chai for #2
# 4s Taking order for #3
# 6s Brewing chai for #3
# 9s All orders taken and chai brewed