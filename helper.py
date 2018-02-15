"""
    This file consists of various helper fucntions 
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"


"""
    There is no 16 bit signed short datatype in python 
    This is way i implement it. I use the method we discussed in class 
    2**n - that number 
    src = https://mail.python.org/pipermail/python-list/2003-April/211404.html
"""
def hex2uint16(s):
     # assumed s is up to four hex digits
     i = eval(s)
     #check if there is an overflow 
     if i >= 2**15:
        # the idea we use here is that a negetive numebr is 2**n - that number
         i -= 2**16
     return i


"""
    This method converts the opcode to the aprropriate instruction
"""
def get_op_value(opcode):
    if(opcode == 0x23):
        return "lw"
    elif(opcode == 0x04):
        return "beq"
    elif(opcode == 0x2b):
        return "sw"
    elif(opcode == 0x05):
        return "bne"


"""
    This method converts the func code to the aprropriate instruction
"""
def get_func_value(func):
    if(func == 0x20):
        return "add"
    elif(func == 0x22):
        return "sub"
    elif(func == 0x24):
        return "and"
    elif(func == 0x25):
        return "or"
