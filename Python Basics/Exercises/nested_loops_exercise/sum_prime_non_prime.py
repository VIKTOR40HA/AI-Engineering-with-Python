prime_total = 0
non_prime_total =0
while True:
    text = input()
    if text == "stop":
        break
    else:
        number = int(text)
        if number < 0:
            print("Number is negative.")
            continue
        is_prime = True
        for num in range(2, number):
            if number % num == 0:
                is_prime = False
                break

        if is_prime:
            prime_total += number
        else:
            non_prime_total += number

print(f"Sum of all prime numbers is: {prime_total}")
print(f"Sum of all non prime numbers is: {non_prime_total}")
