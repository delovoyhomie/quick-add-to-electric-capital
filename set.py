# repositories from https://github.com/electric-capital/crypto-ecosystems/blob/master/data/ecosystems/t/ton.toml
with open('C:/1. MY FILES/1. PROGRAMMING/3. TON/6. Others/electric-capital/list.txt') as list1:
    list1 = list1.read()
    list1 = list1.replace('\n', '')
    list1 = list1.replace('[[repo]]', '')
    list1 = list1.replace('url = "', " ")
    list1 = list1.replace('"', '')
    list1 = list1.split()

# repositories you want to add 
with open('C:/1. MY FILES/1. PROGRAMMING/3. TON/6. Others/electric-capital/DoraHacks Repos.csv') as t:
    list2 = []
    for i in range(126):
        list2.append(t.readline().replace('\n', ''))

# finding duplicates
def intersection_list(list1, list2): 
   return set(list1).intersection(list2) 

print('Intersection:', intersection_list(list1, list2)) 

# removing duplicates from your sheet in repositories
for i in range(len(intersection_list(list1, list2))):
    for j in intersection_list(list1, list2):
        # print(j)
        list2.remove(j)

# print('Intersection:', intersection_list(list1, list2)) 

# sorting lists
done_ls = list1 + list2
done_ls.sort()

# write to final file with all repositories
with open('C:/1. MY FILES/1. PROGRAMMING/3. TON/6. Others/electric-capital/done_list.txt', 'w') as result:
    for i in done_ls:
        result.write('[[repo]] \n' + 'url = "' + i + '"' + '\n\n')
    





