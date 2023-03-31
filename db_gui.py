import tkinter as tk
from tkinter import ttk
import requests


def create_blood_string(blood_letter, rh):
    blood_string = "{}{}".format(blood_letter, rh)
    return blood_string


def id_number_verification(id_number):
    if 1 <= id_number <= 10000000:
        return True
    else:
        return False


def check_and_upload_data(patient_name, id_number, blood_letter, rh,
                          donation_center):
    blood_string = create_blood_string(blood_letter, rh)
    if id_number_verification(id_number) is False:
        return "ID number is incorrect"
    msg = send_data_to_server(patient_name, id_number, blood_string,
                              donation_center)
    return msg


def send_data_to_server(patient_name, id_number, blood_string,
                        donation_center):
    patient = {"id": id_number, "name": patient_name,
               "blood_type": blood_string}
    r = requests.post("http://127.0.0.15000/add_patient")
    return r.text
    

def set_up_window():

    def ok_bt_cmd():
        print("Ok clicked")
        patient_name = name_value.get()
        id_number = id_value.get()
        blood_letter = blood_letter_value.get()
        rh = rh_factor_value.get()
        #print("Patient name is {}".format(patient_name))
        #print("Patient id is {}".format(id_number))
        #print("Patient blood type is {} {}".format(blood_letter, rh))
        donation_center = donation_value.get()
        msg = check_and_upload_data(patient_name, id_number, blood_letter, rh,
                                    donation_center)
        status_label.configure(text=msg)

    def cancel_btn_cmd():
        root.destroy()

    root = tk.Tk()  # Start with Tk widget
    root.title("Donor Database GUI")
    root.geometry("800x800")
    # Add labels and grid
    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky=tk.E)
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1, sticky=tk.E)
    name_value = tk.StringVar()
    # Create entry boxes
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column=1, row=1, padx=5)

    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column=0, row=2, sticky=tk.E)
    id_value = tk.StringVar()
    id_entry = ttk.Entry(root, textvariable=id_value)
    id_entry.grid(column=1, row=2, padx=5)

    ok_button = ttk.Button(root, text="Ok", command=ok_bt_cmd)
    ok_button.grid(column=1, row=6, sticky=tk.E)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_button.grid(column=2, row=6, sticky=tk.E)
    # Make variable to store what selection was made
    blood_letter_value = tk.StringVar()
    A_check = ttk.Radiobutton(root, text="A", variable=blood_letter_value,
                              value="A")
    A_check.grid(column=0, row=3)
    B_check = ttk.Radiobutton(root, text="B", variable=blood_letter_value,
                              value="B")
    B_check.grid(column=0, row=4)
    AB_check = ttk.Radiobutton(root, text="AB", variable=blood_letter_value,
                              value="AB")
    AB_check.grid(column=0, row=5)
    O_check = ttk.Radiobutton(root, text="O", variable=blood_letter_value,
                              value="O")
    O_check.grid(column=0, row=6)

    rh_factor_value = tk.StringVar()
    rh_factor_value.set("-")
    check_box_widget = ttk.Checkbutton(root, text="Rh Positive",
                                        variable=rh_factor_value,
                                        onvalue="+", offvalue="-")
    check_box_widget.grid(column=1, row=4)
    # Tell tkinter to display the window
    donation_label = ttk.Label(root, text="Closest Donation Center")
    donation_label.grid(column=2, row=0)
    donation_value = tk.StringVar()
    donation_combobox = ttk.Combobox(root, textvariable=donation_value)
    donation_combobox.grid(column=2, row=1)
    donation_combobox["values"] = ("Durham", "Apex", "Raleigh")
    donation_combobox.state["readonly"]

    status_label = ttk.Label(root, text="")
    status_label.grid(column=0, row=7, columnspan=10)

    root.mainloop()


if __name__ == "__main__":
    set_up_window()
    print("End")
