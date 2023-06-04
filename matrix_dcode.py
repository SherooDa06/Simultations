import matrices as m
from copy import copy

letters = {
    '!' : -3, ',' : -2, '.' : -1,
    ' ' : 0, 'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13,
    'N' : 14, 'O' : 15, 'P': 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V': 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26,
}

def ensure_proper_list_size(lst, div_factor):
    while (len(lst) % div_factor) != 0:
        lst.append(' ')

def convert_message_to_matrix_array(msg):
    char_array = []
    for char in msg.upper():
        char_array.append(char)
    ensure_proper_list_size(char_array, 4)

    future_matrix_array =[]
    future_matrix = []

    for char in char_array:
        future_matrix.append(char)
        if len(future_matrix) == 4:
            future_matrix_array.append(copy(future_matrix))
            future_matrix.clear()

    output = []
    for mtx in future_matrix_array:
        new_matrix_element = m._2x2_matrix(letters[mtx[0]], letters[mtx[1]], letters[mtx[2]], letters[mtx[3]])
        output.append(copy(new_matrix_element))

        del new_matrix_element

    return output

def convert_matrix_array_to_message(mtx_arr):
    int_array = []
    for mtx in mtx_arr:
        int_array.append(copy(mtx._11))
        int_array.append(copy(mtx._12))
        int_array.append(copy(mtx._21))
        int_array.append(copy(mtx._22))

    char_keys = []
    for key in letters.keys():
        char_keys.append(key)

    char_array = []
    for val in int_array:
        char_array.append(char_keys[val + 3])

    output = ""
    for char in char_array:
        output += char

    return output

def encode_matrix_array(mtx_arr, key):
    output = []
    for mtx in mtx_arr:
        output.append(m.add(mtx, key))

    return output

def decode_matrix_array(mtx_arr, key):
    output = []
    for mtx in mtx_arr:
        output.append(m.subtract(mtx, key))

    return output

def encode_message(msg, key):
    old_mtx_array = convert_message_to_matrix_array(msg)
    new_matrix_array = encode_matrix_array(old_mtx_array, key)
    output = convert_matrix_array_to_message(new_matrix_array)

    return output

def decode_message(msg, key):
    old_mtx_array = convert_message_to_matrix_array(msg)
    new_matrix_array = decode_matrix_array(old_mtx_array, key)
    output = convert_matrix_array_to_message(new_matrix_array)

    return output

message = "YOU MAY BE DISSAPPOINTED BUT YOU CANNOT GLITCH IT"
key = m._2x2_matrix(-1, 1, 1, -1)

encoded_message = encode_message(message, key)
print("Encoded message: " + encoded_message)

decoded_message = decode_message(encoded_message, key)
print("Decoded message: " + decoded_message)