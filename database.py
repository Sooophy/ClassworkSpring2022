def add_patient(patient_name, patient_id, age):
    new_patient = [patient_name, patient_id, age, []]
    return new_patient


def main():
    db = []
    x = add_patient("Ann Ables", 342, 40)
    db.append(x)
    y = add_patient("Bob Boyles", 50, 50)
    db.append(y)
    z = add_patient("Chris Columbus", 111, 35)
    db.append(z)
    db. append(add_patient("David Dinkins", 22, 72))
    found_patient = find_patient(db, 111)
    print(found_patient)
    print(db)
    add_test_to_patient(db, 111, "HDL", 100)
    print(db)
    return db


def find_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return


def add_test_to_patient(db, id_no, test_name, test_result):
    patient = find_patient(db, id_no)
    test_tuple = (test_name, test_result)
    patient[3].append(test_tuple)
    # change the list here, also changes the list of db, list is mutable


def print_direcotry(db):
    rooms = ["Room 13", "Room 12", "Room 99", "Room 3"]
    # zip: iterate 2 lists with the same lenth together
    for room, patient in zip(rooms, db):
        print("{} - {}".format(patient[0], room))
        # print("Name: {}".format(patient[0]))


if __name__ == "__main__":
    db = main()
    print_direcotry(db)
