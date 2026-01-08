with open("day-10/file.txt",'r') as f:
    print(f.tell())
    print(f.seek(19)) #it remove the elements
    print(f.read())