import os

# Input and output file
try:
    os.remove('up-PARCHG')
    os.remove('down-PARCHG')
    raise FileNotFoundError
except FileNotFoundError:
    pass
path = input("Please input the PARCHG file name:")
input_file = open(path)
lines = input_file.readlines()
output_file_up = open('up-PARCHG', mode='a', encoding='utf-8')
output_file_down = open('down-PARCHG', mode='a', encoding='utf-8')

# To find the split line between the Structure and spin-up data.
part1 = 0
Total_length = len(lines)
for i in range(Total_length):
    if lines[i] == ' \n':
        part1 = i + 2
        break

# To fine the split line between the spin-up and spin-down data.
part2 = 0
for i in range(part1 + 1, Total_length):
    if lines[i] == ' \n':
        part2 = i + 2
        break

# Save the spin-up and spin-down parts
for i in range(part1):
    output_file_up.write(lines[i])
    output_file_down.write(lines[i])
for i in range(part1, part2 - 3):
    data1 = lines[i].split()
    data2 = lines[i + part2 - part1].split()
    for j in range(len(data1)):
        data1[j] = eval(data1[j])
        data2[j] = eval(data2[j])
        up = (data1[j] + data2[j]) / 2
        down = (data1[j] - data2[j]) / 2
        up = "{:.6g}".format(up)
        down = "{:.6g}".format(down)
        output_file_up.write(str(up) + " ")
        output_file_down.write(str(down) + " ")
    output_file_up.write('\n')
    output_file_down.write('\n')