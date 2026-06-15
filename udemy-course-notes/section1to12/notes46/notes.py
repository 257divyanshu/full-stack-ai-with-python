# def local_chai():
#     yield "Masala Chai"
#     yield "Ginger Chai"

# def imported_chai():
#     yield "Matcha"
#     yield "Oolong"

# def full_menu():
#     yield from local_chai()
#     yield from imported_chai()

# chai_gen_obj = full_menu()
# print(next(chai_gen_obj))
# print(next(chai_gen_obj))
# print(next(chai_gen_obj))
# print(next(chai_gen_obj))
# print(next(chai_gen_obj))

# for chai in full_menu():
#     print(chai)



def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
            print(f'preparing {order}')
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
stall.send('chaiA')
stall.send('chaiB')
stall.close()

# 🔬 NOTES
# - the first next(stall) starts the generator
# - further next(stall) == stall.send(None)
# - After starting a generator, always use send() consistently if it expects input.
# - Avoid further next() unless you want to send None
# 📍 First next(stall)
# - Generator hasn’t reached yield yet
# - So it runs until first yield
# - No value is being “sent into” order yet
# - This line hasn’t executed yet:
# order = yield ...
# - So no assignment happens.
# 📍 Subsequent next(stall)
# - Generator is paused at yield
# - Now next() behaves like:
# send(None)
# - So order = None
# - The first next() does NOT send anything — it just prepares the generator.