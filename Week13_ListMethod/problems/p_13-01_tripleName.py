def namelist(names):
    name = ''
    for i in range(len(names)):
        if i == len(names) - 1:
            name += names[i]
        elif i == len(names) - 2:
            name += names[i] + ' & '
        else:
            name += names[i] + ', '
    return name

print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Peter']) )
print( namelist([]) == '' )
