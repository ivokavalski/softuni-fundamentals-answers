number_of_orders = int(input())

sum = 0

for i in range(number_of_orders):
    pr_p_capsure = float(input())
    days = int(input())
    cap_per_day = int(input())

    if pr_p_capsure < 0.01 or pr_p_capsure > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif cap_per_day < 1 or cap_per_day > 2000:
        continue

    current_price = pr_p_capsure * cap_per_day * days
    sum += current_price
    print(f"The price for the coffee is: ${current_price}")

print(f"Total: ${sum}")




