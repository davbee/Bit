address = 0x0012

print(address)

addr2 = address >> 4
print(addr2)

addr3 = address << 4
print(addr3)

bit4 = address & 0x10
print(bit4)

bit5 = address & (1 << 4)
print(bit5)
