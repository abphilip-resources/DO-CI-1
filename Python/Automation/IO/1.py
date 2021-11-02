F = open("File.txt",'r')
passFile = open("Pass.txt",'w')
failFile = open("Fail.txt",'w')
for line in F:
    if(line.split()[2]=="P"): passFile.write(line)
    else: failFile.write(line)
passFile.close()
failFile.close()