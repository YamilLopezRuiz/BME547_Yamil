in_file = open("input_data.txt", "r")  # If in another folder have to add more
fruits = in_file.readlines()
print(fruits)
in_file.close()

# in_file = open("input_data.txt", "r")
# # If file is very big, just look for data you want
# for line in in_file:
#    print(line)
# first_fruit = in_file.readline()
# # Reads only one line, but cannot move back up
# second_fruit = in_file.readline()
# # Need to close file and reopen if you want to go up


def analyze_ID(input_line):
    patient_data = input_line.strip("\n").split("=")  # Remove \n from string
    patient_id = int(patient_data[1])
    return patient_id


def read_file(filename):
    in_file = open(filename, "r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)


# def test_read_file():
#     from module import read_file
#     filename = "my_test_data.txt"
#     answer = read_file(filename)
#     expected = 50
#     assert = expected
