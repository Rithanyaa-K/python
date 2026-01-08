with open("day-10/merge1.txt",'r') as f1,open("day-10/merge2.txt",'r') as f2:
    text=f1.read()+f2.read()
with open("day-10/mergedText.txt",'w') as f:
    f.write(text)

