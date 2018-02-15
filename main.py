"""
    This program acts as a MIPS disassembler. 
    Read through the hex instructions and decode it to assembly language instructions
"""

__autor__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"



from constants import *
from helper import *


def main():

    print("MIPS DISASSEMBLER by Aman Nagpal:\n\n")
    pc = PC
    for instr in INSTRUCTIONS:
        opcode = get_shifted_value(instr, OPCODE_MASK, OPCODE_SHIFT)
        src1reg = get_shifted_value(instr, SRC1REG_MASK, SRC1_SHIFT)
        src2reg = get_shifted_value(instr, SRC2_DES_REG_MASK, SRC2_SHIFT)

        if (opcode == 0x00):
            # we are in the R-format type here 
            des_reg = get_shifted_value(instr, DESREG_MASK, DES_SHIFT)
            func = get_shifted_value(instr, FUNC_MASK)

            # change the hex value to appropriate func
            func = get_func_value(func)

            # print the value 
            print("{address}\t{func} ${des_reg}, ${src1_reg}, ${src2_reg}".format(address=hex(pc), func=func, des_reg=des_reg, src1_reg=src1reg, src2_reg=src2reg))
            pc = pc + 0x4


        else:
            # this is where we deal with I-Format
            des_reg = src2reg
            offset = get_shifted_value(instr, OFFSET_MASK)
            offset = hex2uint16(hex(offset))
            opcode = get_op_value(opcode)

            if(opcode != "beq" and opcode != "bne"):
                print("{address}\t{opcode} ${des_reg}, {offset}(${src_reg})".format(address=hex(pc), opcode=opcode, des_reg=des_reg, offset=offset, src_reg=src1reg ))
            
            else:
                #decompress offset
                # target_address = old_pc + 0x4 + (compressed_pc_offest <<< 2) 
                offset <<= 2
                target_address = pc + 0x4 + offset
                print("{address}\t{opcode} {reg1}, {reg2}, address {target}".format(address=hex(pc), opcode=opcode, reg1=src1reg, reg2=src2reg, target=hex(target_address)))

            # increment the pc 
            pc = pc + 0x4
            



"""
    This function does the bitwise and comparision to isolate the particular field 
    It then shifts it to the end 
    :param: instr -> hex value of the instruction 
    :param: bitmask -> The bitmask required to isolate a particular field
    :param: shift -> the number of bits to shift default 0
    :return: temp_value -> The shifted value

"""
def get_shifted_value(instr, bitmask, shift=0):
    # do a bitwise and 
    temp_value = (instr & bitmask)

    # do the logical shift
    temp_value >>= shift

    #return that shifted value
    return temp_value



if __name__ == "__main__":
    main()
