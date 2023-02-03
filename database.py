def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient

def main_driver():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 34))
    db.append(create_patient_entry("Bob Boyles", 2, 45))
    db.append(create_patient_entry("Chris Chou", 3, 52))
    print(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 100)
    #add_test_to_patient(db, 3, "temp", 99)
    room_numbers = ["103", "232", "333"]
    print(db)
#    print_directory(db, room_numbers)
    print(get_test)


#def print_directory(db, room_numbers):
#    for i, patient in enumerate(db):   #enumerate returns the patient and index
#        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
#    for patient, rn in zip(db, room_numbers):   #if list are same length, it'l go trough both at same time
#        print("Patient {} is in room {}".format(patient[0], rn))
    

def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient[1] == mrn_to_find:
            return patient
    return False

def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient == False:
        print("Bad entry")
    else:
        patient[3].append([test_name, test_value])
    return

#write function that will receive medical record # (2) and test name (LDL)
#return the test value
def find_test_value(db, mrn_to_find, test_name):
    patient = get_patient_entry(db, mrn_to_find) #Find the patient with the medical record number
    if patient == False: #If no patient exists, return bad entry
        print("Bad entry")
    elif patient[3][0] == test_name: #for this patient, if the test name
        test_value = patient[3][1]
        return test_value
    
def get_test_value_from_test_list(test_list, test_name):
    for test in test_list: #Goes through to find for the correct test name
        if test[0] == test_name:
            return test[1]
    return False

def get_patient_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_value = get_test_value_from_test_list(db, test_name)
    return test_value
if __name__ == "__main__":
    main_driver()