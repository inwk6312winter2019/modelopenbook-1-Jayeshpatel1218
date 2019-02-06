def replace_ip(file_name):
    file = open(file_name)
    l1 = []
    l2 = [] 
    l3 = [] 
    l4 = [] 
    for line in file:
        line = line.strip()
        for word in line.split():
            l1.append(word)

    for i in range(len(l1)):
        if l1[1-i] != 'no' and l1[i] == 'ip' and l1[i+1] == 'address':
               l2.append(l1[i+2]) 

    for i in l2:
   
