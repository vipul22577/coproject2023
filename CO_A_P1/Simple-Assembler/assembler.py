import sys

# Instruction set
instruction_set = {
    "A": {
        "add": "00000",
        "sub": "00001",
        "mul": "00110",
        "xor": "01010",
        "or": "01011",
        "and": "01100",
    },
    "B": {"mov": "00010", "rs": "01000", "ls": "01001"},
    "C": { "cmp": "01110", "div": "00111", "not": "01101","mov": "00011"},
    "D": {"ld": "00100", "st": "00101"},
    "E": {"jmp": "01111", "jlt": "11100", "jgt": "11101", "je": "11111"},
    "F": {"hlt": "11010"},
}

# Binary representation of registers
registers = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "R6": "110",
    "FLAGS": "111",
}

# Labels
labels = {
    "label1": "0001101",
    "label2": "0001000",
    "label3": "0001100",
    "label4": "0001110",
}

# Helper functions to handle different instruction types

def type_A(ins):
    opcode = instruction_set["A"].get(ins[0])
    if opcode:
        return opcode, "00"



def type_C(ins):
    opcode = instruction_set["C"].get(ins[0])
    if opcode:
        return opcode, "00000"
    
def type_B(ins):
    if (ins[0]=="mov"):
        if (ins[2] in registers):
            opcode,un_bits=type_C(ins)
            return opcode,un_bits
    
    opcode = instruction_set["B"].get(ins[0])

    if opcode:
        return opcode, "0"

def type_D(ins):
    opcode = instruction_set["D"].get(ins[0])
    if opcode:
        return opcode, "0"

def type_E(ins):
    opcode = instruction_set["E"].get(ins[0])
    if opcode:
        return opcode, "0000"

def type_F(ins):
    opcode = instruction_set["F"].get(ins[0])
    if opcode:
        return opcode, "00000000000"

def register_binary(ins, l):
    value = []
    for i in range(1, l):
        reg = registers.get(ins[i])
        if reg:
            value.append(reg)
    return value

def print_binary(ins, l):
    final_value = register_binary(ins, l)
    reg_code = "".join(final_value)
    return reg_code

# Main function to translate instructions to binary

def main():
    instructions = []

    for line in sys.stdin:
        instructions.append(line.strip().split())

    if len(instructions) < 1:
        return

    for ins in instructions:
        l = len(ins)
        opcode = None
        unused_bits = None

        if ins[0] in instruction_set["A"]:
            opcode, unused_bits = type_A(ins)
        elif ins[0] in instruction_set["B"]:
            opcode, unused_bits = type_B(ins)
        elif ins[0] in instruction_set["C"]:
            opcode, unused_bits = type_C(ins)
        elif ins[0] in instruction_set["D"]:
            opcode, unused_bits = type_D(ins)
        elif ins[0] in instruction_set["E"]:
            opcode, unused_bits = type_E(ins)
        elif ins[0] in instruction_set["F"]:
            opcode, unused_bits = type_F(ins)
        if (ins[0] in instruction_set["B"] and ins[2][0]=="$"):
            ch = int(ins[2][1:])
            ch = format(ch, '07b')
            binary_code = opcode + unused_bits + print_binary(ins, l) +ch
            sys.stdout.write(binary_code+"\n")        
        else:
            binary_code = opcode + unused_bits + print_binary(ins, l)         
            sys.stdout.write(binary_code + "\n")


if __name__ == "__main__":
    main()
