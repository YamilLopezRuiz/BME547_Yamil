def interface():
    print("Blood calculator: HDL & LDL")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Cholesterol")
        print("9 - Quit")
        choice = input("Select an option:")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            chol_driver()
    print("Program Ending")

def HDL_driver():
    HDL_in = generic_input("HDL")
    HDL_analy = HDL_analysis(HDL_in)
    generic_output("HDL", HDL_in, HDL_analy)


def generic_input(test_name):
    value = input("Enter the {} value:".format(test_name))
    value = int(value)
    return value


def LDL_driver():
    LDL_in = generic_input("LDL")
    LDL_analy = LDL_analysis(LDL_in)
    generic_output("LDL", LDL_in, LDL_analy)


def chol_driver():
    chol_in = generic_input("Cholesterol")
    chol_analy = chol_analysis(chol_in)
    generic_output("Cholesterol", chol_in, chol_analy)


def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def LDL_analysis(LDL_int):
    if LDL_int < 130:
        answer = "Normal"
    elif 130 <= LDL_int <= 159:
        answer = "Borderline High"
    elif 160 <= LDL_int <= 189:
        answer = "High"
    else:
        answer  = "Very High"
    return answer


def chol_analysis(chol_int):
    if chol_int < 200:
        answer = "Normal"
    elif 200 <= chol_int < 240:
        answer = "Borderline High"
    elif chol_int >= 240:
        answer = "High"
    return answer


def generic_output(test_name, test_value, test_analy):
    print("The {} result of {} is considered {}"
        .format(test_name, test_value, test_analy))
    return 



if __name__ == "__main__":
    interface()
