# program E11x13.py
# Writing to a binary file and reading
outfile=open("b1", 'wb+') # for reading and writing     
outfile.write(b'123')
outfile.write(b'456')
outfile.write(b'789')
for i in range (0,12,3):
    outfile.seek(i)
    print(outfile.tell())
    print(outfile.read(3))
outfile.close()
