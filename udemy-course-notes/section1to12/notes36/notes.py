# def make_chai():
#     return "Here is your masal chai"
#     # print("Here is your masala chai")
# return_value = make_chai()
# print(return_value)

# def idle_chaiwala():
#     pass
# print(idle_chaiwala()) # None

# def sold_cups():
#     return 120
# total = sold_cups()
# print(total) # 120

# def chai_status(cups_left):
#     if cups_left == 0:
#         return "Sorry, chai over"
#     return "Chai is ready"
#     print("chai")
# print(chai_status(0))
# print(chai_status(5))

def chai_report():
    return 100, 20, 10 # sold, remaining, not_paid
# report = chai_report()
# print(type(report)) # <class 'tuple'>
sold, remaining, not_paid = chai_report()
print("Sold: ", sold)
print("Remaining: ", remaining)
print("Not Paid: ", not_paid)