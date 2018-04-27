in_file = open("inputfile.txt", "r")
out_file = open("outfile.txt", "w")

stack = in_file.readlines()
in_file.close()

length = len(stack)

for i in range(length):
    j = length - i - 1
    if stack[i] == '':
        continue
    out_file.write(stack[j])

out_file.close()
