"""
    This file consists of various constants that we would be using in out program
    These constants include things like OPCODES, 
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"


INSTRUCTIONS = [0x032ba020, 0x8ce90014, 0x12a90003, 0x022DA822, 0xADB30020, 0x02697824, 0xAE8FFFF4, 0x018C6020, 0x02A4A825, 0x158FFFF7, 0x8ECDFFF0]

OPCODE_MASK= 0xfc000000
SRC1REG_MASK=  0x03e00000
SRC2_DES_REG_MASK = 0x001f0000
DESREG_MASK = 0x0000f800
OFFSET_MASK = 0x0000FFFF
FUNC_MASK = 0x0000003f



# shifting values 
OPCODE_SHIFT = 26
SRC1_SHIFT = 21
SRC2_SHIFT = 16
DES_SHIFT = 11


#DEFAULT PC 
PC = 0x9a040

