f=open("day-10/file.txt",'r')
readOperation=f.read() #read declare it shows all sentences but readline show only 1 line and readlines means reading in list format
print(readOperation)
f.close()

f=open("day-10/file.txt",'r')
readLineOperation=f.readline()
print(readLineOperation)  
f.close()

f=open("day-10/file.txt",'r')
readLinesOperation=f.readlines()
print(readLinesOperation)
f.close()         #global