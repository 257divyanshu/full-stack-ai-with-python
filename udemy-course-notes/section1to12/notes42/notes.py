daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# total_cups = sum(sale for sale in daily_sales if sale > 5)
# print(total_cups)

total_cups = sum([sale for sale in daily_sales if sale > 5]) # this too works
print(total_cups)

# ❔1️⃣ if sum accepts an 'iterable' as the first argument, why using a generator expression worked fine?

print(help(sum))
# print(sum([1,2,3,4,5])) # 15