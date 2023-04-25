#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


# m = b"keepcoding"
# k = b"abcdefghij"

m1 = bytes("España","utf-8")

m = bytes("keepcoding===","utf-8")
k = bytes("abcdefghijddd","utf-8")

print(xor_data(m,k))
print(xor_data(m,k).hex())

# =====
print(xor_data(m,k).hex())

