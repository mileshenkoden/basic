inputfile = "rockyou.txt"
outpudfile = "my_paswords.txt"

pasword_for_denys = "denys"

my_file_read = open(inputfile, mode="r", encoding="utf-8")
my_file_apend = open(outpudfile, mode="a", encoding="utf-8")

#print(my_file.read())

for num, line in enumerate(my_file_read, 1):
    if pasword_for_denys in line:
        print("line number", str(num) , line.strip())
        my_file_apend.write("pasword with name danys:" + line)

my_file_apend.close()
my_file_read.close()