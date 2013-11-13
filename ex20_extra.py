def print_line(x, y):
    print "%s %s" %(x, y.readline())

input_file = raw_input("pls input your file:")
current_file = open(input_file)
line_number = 1

print_line(line_number, current_file)

line_number = line_number + 1

print_line(line_number, current_file)

##############################################
#Below code is not correct.
test = """
def print_line(x,y):
    print "%s %s" %(x, y)

input_file = raw_input ("pls input you file:")
current_file = open(input_file)
line_number = 1
current_content = current_file.readline()

print_line(line_number, current_content)

line_number = line_number + 1

print_line(line_number, current_content)
"""
