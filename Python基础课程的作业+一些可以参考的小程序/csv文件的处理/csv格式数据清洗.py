f=open("data.csv")
line=f.readlines()
line.reverse()
print(line)
for i in line:
    i=i.replace('\n','')
    i=i.replace(' ','')
    a=i.split(",")
    a.reverse()
    print(";".join(a))