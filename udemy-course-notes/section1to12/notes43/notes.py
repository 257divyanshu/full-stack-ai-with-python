# def serve_chai():
#     yield "Cup 1: Masala Chai"
#     yield "Cup 2: Ginger Chai"
#     yield "Cup 3: Elaichi Chai"

# stall = serve_chai()

# print(stall) # <generator object serve_chai at 0x000001E6419F53C0>
# print(next(stall)) # "Cup 1: Masala Chai"
# print(next(stall)) # "Cup 2: Ginger Chai"
# print(next(stall)) # "Cup 3: Elaici Chai"
# print(next(stall)) # StopIteration Error

# for cup in stall:
#     print(cup)

# ---------------------------------------------

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
# def get_chai_gen():
#     yield "Cup 1"
#     yield "Cup 2"
#     yield "Cup 3"

# chai = get_chai_gen()
# print(next(chai))
# print(next(chai))
# print(next(chai))
# print(next(chai)) # gives error