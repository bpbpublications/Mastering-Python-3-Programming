# program E11x12.py
# Writing to a binary file and reading
outfile=open("b1", 'wb+') # for reading and writing     
outfile.write(b'123')
outfile.write(b'456')
outfile.write(b'789')
for i in range (12):
    outfile.seek(i)
    print(outfile.tell())
    print(outfile.read(1))  
outfile.close()
