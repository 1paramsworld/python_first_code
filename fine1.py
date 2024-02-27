start = 10
end = 50

prime_numbers = []

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

print("Prime numbers between", start, "and", end, ":", prime_numbers)

