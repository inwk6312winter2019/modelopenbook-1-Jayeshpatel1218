def list_ifname_ip(file_name):
        file=open(file_name)
        l1 = []
        l2 = []
        l3 = []
        dict={} 
        for line in file:
                line=line.strip()
                for word in line.split():
                        l1.append(word)
        for i in range(len(l1)):
            if l1[i]=='no' and l1[i+1]=='nameif':
                l2.append('no ip address')
                                l3.append('no netmask')
            elif l1[i-1]!='no' and l1[i]=='nameif':

