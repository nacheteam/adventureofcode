BANKS = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"

# Format the list to int array.
bank_list = BANKS.split('\t')
for i in range(len(bank_list)):
    bank_list[i] = int(bank_list[i])

# Keep track of the previous configs
configuration = ' '.join(map(str,bank_list))
previous_configurations = []
redistributions = 0
while configuration not in previous_configurations:
    previous_configurations.append(configuration)
    mx = max(bank_list)
    index = bank_list.index(mx)
    bank_list[index]=0
    for i in range(1,mx+1):
        bank_list[(index+i)%len(bank_list)] += 1
    configuration = ' '.join(map(str,bank_list))
    redistributions+=1

print(redistributions)
