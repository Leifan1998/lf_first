import struct


def relu(x):
    if x >= 0:
        return x
    else:
        return 0

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


def hex_to_float(h):
    return struct.unpack('<f', struct.pack('<I', int(h, 16)))[0]



def float_mul(num_1, num_2):
    result = num_1 * num_2
    return result


def float_add(num_1, num_2):
    result = num_1 + num_2
    return result

x = 1.25                    # IEEE 754标准-0x3fa00000
w = 0.09999999403953552     # IEEE 754标准-0x3dcccccc
b = 0.09999999403953552     # IEEE 754标准-0x3dcccccc


Layer11 = float_add(float_add(float_add(float_mul(x, w), float_mul(x, w)), float_mul(x, w)), b)
Layer12 = float_add(float_add(float_add(float_mul(x, w), float_mul(x, w)), float_mul(x, w)), b)
Layer13 = float_add(float_add(float_add(float_mul(x, w), float_mul(x, w)), float_mul(x, w)), b)

Layer21 = float_add(float_add(float_add(float_mul(Layer11, w), float_mul(Layer12, w)), float_mul(Layer13, w)), b)
Layer22 = float_add(float_add(float_add(float_mul(Layer11, w), float_mul(Layer12, w)), float_mul(Layer13, w)), b)
Layer23 = float_add(float_add(float_add(float_mul(Layer11, w), float_mul(Layer12, w)), float_mul(Layer13, w)), b)

Layer31 = float_add(float_add(float_add(float_mul(Layer21, w), float_mul(Layer22, w)), float_mul(Layer23, w)), b)
Layer32 = float_add(float_add(float_add(float_mul(Layer21, w), float_mul(Layer22, w)), float_mul(Layer23, w)), b)
Layer33 = float_add(float_add(float_add(float_mul(Layer21, w), float_mul(Layer22, w)), float_mul(Layer23, w)), b)

Y1 = relu(Layer31)
Y2 = relu(Layer32)
Y3 = relu(Layer33)

Y1_result = float_to_hex(Y1)
Y2_result = float_to_hex(Y2)
Y3_result = float_to_hex(Y3)

print(Y1_result)  #output:0x3e30e55f
print(Y2_result)  #output:0x3e30e55f
print(Y3_result)  #output:0x3e30e55f











