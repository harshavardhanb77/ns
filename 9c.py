out=open("text.txt",'w')
out.write('Functions\nLine no\t code line\n')
with open('10a.py','r') as ip:
    for i,j in enumerate(ip.readlines(),1):
        if j.strip().startswith("def"):
            print(j.strip()[:-1])
            out.write(str(i)+'\t'+j.strip()[:-1]+'\n')
out.write('Leaders\nLine no\t code line\n')           
with open('10a.py','r') as ip:
    for i,j in enumerate(ip.readlines(),1):
        if j.strip().endswith(":"):
            print(j.strip()[:-1])
            out.write(str(i)+'\t'+j.strip()[:-1]+'\n')
out.close()