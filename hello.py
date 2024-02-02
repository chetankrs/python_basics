def primes(n: int):
    """Return a list of the first n primes."""
    sieve = [True] * n

    res = []

    for i in range(2, n):
        if sieve[i]:
            res.append(i)
            for j in range(i * i, n, i):
                sieve[j] = False

    return res


xs = primes(100)

print(xs)

message = "try CaSES with thIS STRing."
print(message.title())

first_name = "chetan"
last_name = "kumar"

full_name = f"{first_name} {last_name}"

print(full_name)

MAX_CONNECTIONS = 5_000
print(MAX_CONNECTIONS)

MAX_CONNECTIONS = 40_00
print(MAX_CONNECTIONS)

a_list = ["a", "b", "c", "d", "e"]

print(a_list[0])
print(a_list[-1])

letter = f"The letter is {a_list[0].title()}"
print(letter)

print("====================================")

cars = ["bmw", "merc", "audi", "toyota", "ferrari"]

print(sorted(cars))
print(cars)

cars.sort(reverse=True)
print(cars)
