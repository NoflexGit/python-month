alcohol_permit_age = 18

guys = [{'name': 'Jane', 'age': 17}, {
    'name': 'Richi', 'age': 21}, {'name': 'James', 'age': 20}, ]

for item in guys:
    if(item['age'] >= alcohol_permit_age):
        print(f"{item['name']} can buy alcohol")
    else:
        print(f"{item['name']} can't buy alcohol")
