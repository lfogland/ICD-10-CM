with open ("icd10cm.txt", encoding="utf-8")
as f:
    lines = f.readlines()

codes = []
for line in lines:
    parts = line.strip().split("\t")
    if len(parts) == 2:
        codes.append((parts[0], parts[1]))

while True:
    search = input("Enter ICD-10-CM code or description: ").lower()
    if search == "quit":
        print("Goodbye!")
        break

    matches = []
    for code, desc in codes:
        if search in code.lower() or search in desc.lower():
            matches.append((code, desc))
    if matches:
        print(f"\nFound {len(matches)} match(es):")
        for code, desc in matches:
            print(f"{code} - {desc}")
    else:
        print("No mathces found.")
    again = input("\nWould you like to search again? (Yes/No): ").lower()
    if again != "yes":
        print("Goodbye!")
        break