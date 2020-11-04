import struct

num1 = 12936522
num2 = 123
num3 = 8

ret = struct.pack('i',num1)
print(len(ret))

ret = struct.pack('i',num2)
print(len(ret))

ret = struct.pack('i',num3)
print(len(ret))




