# 📍 Wrong way:
def chai_order(order=[]):
    order.append("Masala")
    print(order)
# chai_order()
# chai_order()
# 📍 Safe way:
# def chai_order(order=None):
#     if order is None:
#         order = []
#     print(order)
# chai_order()
# chai_order()
# 📍 Problem: Default mutable arguments like [] persist across calls
# - what does that problem mean?
# - see doubt.md