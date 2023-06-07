import sys
register_value=["0000000000000000","0000000000000000", "0000000000000000",
                "0000000000000000", "0000000000000000","0000000000000000", "0000000000000000",
                "0000000000000000"]
def typeA(opncode,dstr,src1,src2,Progcntr):
    if opncode=="00000":
        x=int(register_value[int(src1,2)],2)
        y=int(register_value[int(src2,2)],2)
        if x+y>=2**16:
            register_value[int("111",2)]="0000000000001000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
        else:
            register_value[int(dstr,2)]==bin(x+y)[2:].zfill(16)
            register_value[int("111",2)]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)

    if opncode=="00001":
        x=int(register_value[int(src1,2)],2)
        y=int(register_value[int(src2,2)],2)
        if x-y<0:
            register_value[int("111",2)]="0000000000001000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
        else:
            register_value[int(dstr,2)]=bin(x-y)[2:].zfill(16)
            register_value[int("111",2)]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)


    if opncode=="00110":
        x=int(register_value[int(src1,2)],2)
        y=int(register_value[int(src2,2)],2)
        if x*y>=2**16:
            register_value[int("111",2)]="0000000000001000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
        else:
            register_value[int(dstr,2)]==bin(x*y)[2:].zfill(16)
            register_value[int("111",2)]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)


    if opncode=="01010":
        x=int(register_value[int(src1,2)],2)
        y=int(register_value[int(src2,2)],2)
        register_value[int(dstr,2)]=bin(x^y)[2:].zfill(16)
        register_value[int("111",2)]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)
        
        


    if opncode=="01011":
        
        x=int(register_value[int(src1,2)],2)
        y=int(register_value[int(src2,2)],2)
        register_value[int(dstr,2)]=bin(x|y)[2:].zfill (16)
        register_value[int("111",2)]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)


    if opncode=="01100":
        
        x=int(register_value[int(src1,2)],2)
        y=int(register_value[int(src2,2)],2)
        register_value[int(dstr,2)]=bin(x&y)[2:].zfill (16)
        register_value[int("111",2)]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)



def typeB(opncode,dstr,src1,Progcntr):
    if opncode=="00010":
        register_value[int(dstr,2)]=src1
        register_value[int("111",2)]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)
        

        
    if opncode=="01000":
        register_value[int(dstr,2)]=bin(int(register_value[dstr],2) >>int(src1,2))[2:].zfill(16)
        register_value[int("111",2)]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)
        
    
    if opncode=="01001":
        register_value[dstr]=bin(int(register_value[dstr],2)<<int(src1,2))[2:].zfill (16)
        register_value[int("111",2)]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)


def typeC(opncode,dstr,src1,Progcntr):
    if opncode=="00011":
        register_value[int(dstr,2)]=register_value[int(src1,2)]
        register_value[int("111",2)]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)

    elif opncode=="00111":
        if register_value[int(src1,2)]=="0000000000000000":
            register_value[int("111",2)]="0000000000001000"
            register_value[0]="0000000000000000"
            register_value[1]="0000000000000000"
            
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
            
        else:
            quotient=register_value[dstr]/register_value[2]
            remain=register_value[dstr]%register_value[2]
            register_value[0]=bin(quotient)[2:0].zfill(16)
            register_value[1]=bin(remain)[2:0].zfill(16)
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
    elif opncode=="01101":
        x=int(register_value[dstr],2)
        y=int(register_value[src1],2)
        register_value[int(dstr,2)]=bin(~y)[2:].zfill(16)
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)
        
    elif opncode=="01110":
        x=int(register_value[int(dstr,2)],2)
        y=int(register_value[int(src1,2)],2)
        if x>y:
            register_value[3]="0000000000000010"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
            
        elif y>x:
            register_value[3]="0000000000000100"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
        elif y==x:
            register_value[3]="0000000000000001"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
            
def typeD(opncode,dstr,src1,Progcntr):
    if opncode=="00100":
        register_value[int(dstr,2)]=memory_addresses[int(src1,2)]
        register_value[3]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)
    elif opncode=="00101":
        memory_addresses[int(src1,2)]=register_value[int(dstr,2)]
        register_value[3]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=int(Progcntr,2)+1
        execution(Progcntr)
            


def typeE(opncode,dstr,Progcntr):
    if opncode=="01111":
        register_value[3]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        Progcntr=bin(instruction.index(memory_addresses[int(dstr,2)])).zfill(16)
        execution(Progcntr)
    elif opncode=="11101":
        if register_value[3][13]=="1":
            register_value[3]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=bin(instruction.index(memory_addresses[int(dstr,2)])).zfill(16)
            execution(Progcntr)
        else:
            register_value[3]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
    elif opncode=="11101":
        if register_value[3][14]=="1":
            register_value[3]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=bin(instruction.index(memory_addresses[int(dstr,2)])).zfill(16)
            execution(Progcntr)
        else:
            register_value[3]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
    elif opncode=="11111":
        if register_value[3][15]=="1":
            register_value[3]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=bin(instruction.index(memory_addresses[int(dstr,2)])).zfill(16)
            execution(Progcntr)
        else:
            register_value[3]="0000000000000000"
            output=Progcntr+"        "
            output+= " ".join(register_value)
            print(output+"\n")
            Progcntr=int(Progcntr,2)+1
            execution(Progcntr)
               
def typeF(opncode,Progcntr):

    if opncode=="11010":
        register_value[3]="0000000000000000"
        output=Progcntr+"        "
        output+= " ".join(register_value)
        print(output+"\n")
        for i in memory_addresses:
            print(i)
        exit()
        
           
flags = "0000000000000000"

type_mapping = {
    "00000": "A",
    "00001": "A",
    "00010": "B",
    "00011": "C",
    "00100": "D",
    "00101": "D",
    "00110": "A",
    "00111": "C",
    "01000": "B",
    "01001": "B",
    "01010": "A",
    "01011": "A",
    "01100": "A",
    "01101": "C",
    "01110": "C",
    "01111": "E",
    "11100": "E",
    "11101": "E",
    "11111": "E",
    "11010": "F",
}

instruction = []
memory_addresses = []






def execution(ins_no):
 
    program_counter = bin(ins_no)[2:].zfill(7)
    new_reference = instruction[ins_no]
    address = new_reference[0:5]
    
    for element in type_mapping:
        if element == address:
            position = type_mapping[element]
            if position == "A":
                typeA(new_reference[0:5], new_reference[7:10], new_reference[10:13], new_reference[13:16], program_counter)
            elif position == "B":
                typeB(new_reference[0:5], new_reference[6:9], new_reference[9:16], program_counter)
            elif position == "C":
                typeC(new_reference[0:5], new_reference[10:13], new_reference[13:16], program_counter)
            elif position == "D":
                typeD(new_reference[0:5], new_reference[6:9], new_reference[9:16], program_counter)
            elif position == "E":
                typeE(new_reference[0:5], new_reference[9:16], program_counter)
            elif position == "F":
                
                typeF(new_reference[0:5],program_counter)

def main():
    with open("/Users/vipulverma/Downloads/CO_A_P1 (3)/CO_A_P1/SimpleSimulator/binary.txt", "r") as f:
        count = 0
        # for line in sys.stdin:
        for line in f.readlines():
            count += 1
            instruction.append(line.strip())
            memory_addresses.append(line.strip())
            if line[0:5] == "11010":
                break
        for i in range(128 - count):
            memory_addresses.append("0000000000000000")
        execution(0)
main()
