from capstone import *
from capstone.x86 import *

code = bytes.fromhex('b8 02 00 00 00 bb 03 00 00 00 03 c3')
    
assert code is not None

# Setup disassembly engine for x86 32-bit
cs = Cs(CS_ARCH_X86, CS_MODE_32) 
cs.detail = True
cs.skipdata = True

# Create regsiters
registers = {}
registers[X86_REG_EAX] = 0
registers[X86_REG_EBX] = 0

# EIP is our instruction pointer
# Start it at the beginning of the shellcode
registers[X86_REG_EIP] = 0

# Run until we reach the end of the shellcode
while registers[X86_REG_EIP] != len(code):
    address = registers[X86_REG_EIP]
    
    # We don't know the instruction length so choose the maximum size (15)
    # Capstone will truncate accordingly 
    instruction = next(cs.disasm(code[address:address + 15], address))
    mnemonic = instruction.mnemonic
    operands = instruction.operands
    
    # Debug print
    print(f"{address:#010x}:\t{instruction.mnemonic}\t{instruction.op_str}")

    # Instruction handlers (this is our emulator)
    if mnemonic == "mov": 
        # mov <reg>,<imm>
        if operands[0].type == X86_OP_REG and operands[1].type == X86_OP_IMM: 
            registers[operands[0].reg] = operands[1].value.imm
        else:
            print(f"\n{instruction.mnemonic} variation not implemented")
            break
      
    elif mnemonic == "add": 
        # add <reg>,<reg>
        if operands[0].type == X86_OP_REG and operands[1].type == X86_OP_REG: 
            registers[operands[0].reg] = registers[operands[0].reg] + registers[operands[1].reg]
        else:
            print(f"\n{instruction.mnemonic} variation not implemented")
            break
    
    else:
        # Catch unimplemented instruction and exit
        print(f"\nInstruction not implemented: {instruction.mnemonic}")
        break
    
    # Increment EIP to the next instruction
    registers[X86_REG_EIP] += instruction.size

print(f"\nCompleted emulation, EAX: {registers[X86_REG_EAX]}") 