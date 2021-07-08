import argparse

parser = argparse.ArgumentParser()
parser.add_argument("INPUT_FILE")
parser.add_argument("OUTPUT_FILE")
args = parser.parse_args()

input_file = open(args.INPUT_FILE, "rb")
output_file = open(args.OUTPUT_FILE, "w")

output_file.write("""#include "stdlib"
const uint8_t mon_image[] = {
""")

bytes_array = []
while input_file.peek(1) != b'' :
    bytes_array.append("\\0x" + input_file.read(1).hex())

print("Il y a {} octets dans le fichier".format(len(bytes_array)))

data = ""
for n, repr in enumerate(bytes_array):
    data += repr +', '
    if n%8 == 7:
        data+= "\n"
output_file.write(data)
output_file.write("""
};""")

input_file.close()
output_file.close()