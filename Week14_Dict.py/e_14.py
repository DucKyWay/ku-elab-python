# 01-01
months = {
    'jan': "January", 
    'feb': "February", 
    'mar': "March", 
    'apr': "April", 
    'may': "May", 
    'jun': "June", 
    'jul': "July", 
    'aug': "August", 
    'sep': "September", 
    'oct': "October", 
    'nov': "November", 
    'dec': "December"
}

provinces = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
} #Bangkok:central

# 02-01
while True:
    txt = input()
    if txt == '': break
    [pro, re] = txt.split(':')
    if re not in provinces or (pro not in provinces[re]):
        print("No")
        continue
    if pro in provinces[re]: print("Yes")
    else: print("No")
        
# 02-02
for i in provinces:
    for j in provinces[i]:
        print(f"{j}:{i}")
        
# 03-01
while True:
    txt = input()
    if txt == '': break
    [pro, re] = txt.split(':')
    provinces[re].append(pro)
    
# 04-01
countries = {'th': 'Thailand', 'en': "England", "jp": 'Japan', "kr": "Korea"}
value = countries.pop('th')  # ลบ key 'th' ออก
print(value, countries, sep=' | ')

# 04-02
countries = {'th': 'Thailand', 'en': "England", "jp": 'Japan', "kr": "Korea"}
countries.clear()
print(value, countries, sep=' | ')
