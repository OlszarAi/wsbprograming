def split_name(text):
    x = text.split(" ")[0]
    y = text.split(" ")[1]
    return x , y
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(split_name("adam Olszar"))

print(factorial(5))