from random import randint as ran

gen_list = [ran(1,23) for x in range(1,100)]
str_output = ', '.join(str(e) for e in gen_list)

with open(r'input.txt', 'w') as input_txt:
    input_txt.write(str_output)

def compress(input_file):
    pass

def unpack(rle_file):
    pass