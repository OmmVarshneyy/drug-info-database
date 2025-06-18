# Drug Information Database with Add Feature

drugs = [
    {
        "name": "Paracetamol",
        "use": "Pain relief, fever",
        "dosage": "500 mg every 6 hours",
        "side_effects": "Liver damage in high doses"
    },
    {
        "name": "Ibuprofen",
        "use": "Pain, inflammation",
        "dosage": "400 mg every 8 hours",
        "side_effects": "Stomach ulcers, kidney issues"
    },
    {
        "name": "Amoxicillin",
        "use": "Bacterial infections",
        "dosage": "500 mg every 8 hours",
        "side_effects": "Nausea, diarrhea, rash"
    },
    {
        "name": "Cetirizine",
        "use": "Allergies",
        "dosage": "10 mg once daily",
        "side_effects": "Drowsiness, dry mouth"
    }
]

def search_drug(name):
    for drug in drugs:
        if drug["name"].lower() == name.lower():
            print("\n✅ Drug Found!")
            print(f"Name        : {drug['name']}")
            print(f"Use         : {drug['use']}")
            print(f"Dosage      : {drug['dosage']}")
            print(f"Side Effects: {drug['side_effects']}")
            return
    print("\n❌ Drug not found in the database.")

def add_drug():
    print("\n🆕 Add a New Drug")
    name = input("Enter drug name: ").strip()
    use = input("Enter use: ").strip()
    dosage = input("Enter dosage: ").strip()
    side_effects = input("Enter side effects: ").strip()

    # Check if drug already exists
    for drug in drugs:
        if drug["name"].lower() == name.lower():
            print("⚠️ Drug already exists!")
            return

    # Add the new drug
    new_drug = {
        "name": name,
        "use": use,
        "dosage": dosage,
        "side_effects": side_effects
    }
    drugs.append(new_drug)
    print(f"✅ {name} added to the database.")

def view_all_drugs():
    print("\n📄 All Drugs in the Database:")
    for drug in drugs:
        print(f"- {drug['name']}")

def main():
    print("💊 Welcome to the Drug Information Database 💊")
    while True:
        print("\nChoose an option:")
        print("1. Search for a drug")
        print("2. Add a new drug")
        print("3. View all drugs")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            name = input("Enter drug name to search: ").strip()
            search_drug(name)
        elif choice == "2":
            add_drug()
        elif choice == "3":
            view_all_drugs()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
