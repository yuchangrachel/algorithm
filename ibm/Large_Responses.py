'''
https://leetcode.com/discuss/interview-question/406138/ibm-oa-2019-large-responses-backend
'''
from collections import defaultdict

# prompt user input in cli
filename = input()
count = 0 # count how many requests more than 5000bytes
total = 0 # calculate totol sum of bytes more than 5000bytes
with open(filename) as file:
    for line in file:
        line_list = line.split(" ")
        curByte = (int)(line_list[len(line_list) - 1])
        if curByte > 5000:
            count += 1
            total += curByte
    newfile = open("bytes_" + filename, "w")
    newfile.write(str(count) + "\n" + str(total) + "\n")
    newfile.close()
    file.close()
