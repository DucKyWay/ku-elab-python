def extract_atoms(formula):
    res = {}
    element, amount = '', ''
    element = formula[0]
    for i in formula:
        if i.isupper() and element != '':
            res[i] = 0
    return 0

formula = input()
atom = input()
atoms = extract_atoms(formula)
print(atoms.get(atom, 0))