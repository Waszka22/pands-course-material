# this takes a very long time to run

def sqrt(number):
    epsilon = 0.000000000000001
    guess = number / 2.0
    while abs(guess * guess - number) > epsilon:
        guess = (guess + number / guess) / 2.0
    return round(guess, 20)

if __name__ == "__main__":
    number = float(input("Please enter a positive number: "))
    result = sqrt(number)
    print("The square root of", number, "is approx.", result)
