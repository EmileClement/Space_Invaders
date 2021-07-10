import argparse

parser = argparse.ArgumentParser()
parser.add_argument("INPUT_FILE", help="Path vers le fichier d'entrée")
parser.add_argument("HEADER_NAME", help="Path pour le fichier de sortie")
parser.add_argument("VAR_NAME", help="Nom de la varriable à crée")

args = parser.parse_args()

input_file = open(args.INPUT_FILE, "rb")
output_file = open(args.HEADER_NAME+".h", "w")

output_file.write("""#ifndef INC_{}_H_
#define INC_{}_H_

#include "stdint.h"
uint8_t {}[] = """.format(args.HEADER_NAME.upper(), args.HEADER_NAME.upper(), args.VAR_NAME) + """{
""")

bytes_array = []
while input_file.peek(1) != b'' :
    bytes_array.append("0x" + input_file.read(1).hex())

print("Il y a {} octets dans le fichier".format(len(bytes_array)))

data = ""
for n, repr in enumerate(bytes_array):
    data += repr +', '
    if n%8 == 7:
        data+= "\n"
output_file.write(data)
output_file.write("""
};"""+"""

#endif /* INC_{}_H_ */
""".format(args.HEADER_NAME.upper()))

input_file.close()
output_file.close()