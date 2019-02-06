myfile = open("running-config.cfg")
mylist_ifname_ip=[]



for line in myfile:
  
    line = line.strip()
    line = line.split()
if(line[0] == "interface"):
    mylist_ifname_ip.append(line[1])

print(mylist_ifname_ip)
