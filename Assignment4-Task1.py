try:
    file=open('sample.txt','r')
    print("Reading file content:")
    reading_file=file.readline()
    print("Line1:",reading_file.strip())
    reading_file2=file.readline()
    print("Line2:",reading_file2.strip())
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
