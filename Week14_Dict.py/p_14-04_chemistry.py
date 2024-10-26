def extract_atoms(formula):
    res = {}

    i = 0
    while i < len(formula):
        if formula[i].isalpha() and formula[i].isupper():
            element = formula[i]
            i += 1
        
            if i < len(formula) and formula[i].isalpha() and formula[i].islower():
                element += formula[i]
                i += 1

            amount = ''
            while i < len(formula) and formula[i].isdigit():
                amount += formula[i]
                i += 1
            amount = int(amount) if amount else 1

            if element in res:
                res[element] += amount
            else: res[element] = amount
    return res

formula = input()
atom = input()
atoms = extract_atoms(formula)
# for element, amount in atoms.items():
#     print(f"{element}: {amount}")
# print("=============")
if atom not in atoms:
    print(0)
else: print(atoms[atom])