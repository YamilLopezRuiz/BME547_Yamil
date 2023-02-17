a = "The sky is blue"
print(a)

for letter in a:
    print(letter)

fruits = ["apple", "banana", "orange", "cherry", "kiwi"]


def my_function():
    # creates an error
    for i in fruits:
        print(i)
    fruit_len = len(fruits)
    try:
        fruit = fruits[fruit_len]
    except IndexError:
        print("Error found")
        fruit_len = fruit_len - 1
    print(fruits[fruit_len])


def main():
    my_function()


if __name__ == "__main__":
    main()
