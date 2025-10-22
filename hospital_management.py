def search_patients():
    count = int(input("Enter number of patients: "))
    patients = []
    for i in range(count):
        name = input("Enter patient name: ")
        age = int(input("Enter age: "))
        disease = input("Enter disease: ")
        patients.append({"Name": name, "Age": age, "Disease": disease})
    search = input("Enter disease to search for: ")
    found = [p["Name"] for p in patients if p["Disease"] == search]
    print("Patients with", search, ":", found)

if __name__ == "__main__":
    search_patients()
