#Q4

yours = ['Yale', 'MIT', 'Berkeley']
mine = ['Michigan', 'Yale', 'Harvard']
print(yours)
print(mine)

ours1= mine + yours

ours2=[]
ours2.append(mine)
ours2.append(yours)

print(ours1)
print(ours2)


yours[1]= 'Emory'
print(yours)

print(ours1)
print(ours2)

#1
#ours 1 does not distinguish or separate 'mine' from 'yours',
## but ours 2 group 'mine' and 'yours' separately as a separate list

#2
#ours1 is not mutatable because it is a string operation, but ours2 is mutatable because it remained as a list.
#A list is mutatable, therefore, the change in 'yours' group is reflected.
