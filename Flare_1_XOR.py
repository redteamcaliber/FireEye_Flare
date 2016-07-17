#!/usr/bin/env python
'''
	Single Byte XOR decoding for FireEye Flare challenges.
'''

encoded_string = 0x1F, 0x08, 0x13, 0x13, 0x04, 0x22, \
				 0x0E, 0x11, 0x4D, 0x0D, 0x18, 0x3D, \
				 0x1B, 0x11, 0x1C, 0x0F, 0x18, 0x50, \
				 0x12, 0x13, 0x53, 0x1E, 0x12, 0x10


def singlebyte_XOR_decode(encoded_string, xorVal):
	'''
		Name: singlebyte_XOR_decode
		Parameters:
					encoded_string: byte array/list of bytes.
					xorVal:
		Return: List of char's that have been xor'd with xorVal.
	'''
	plaintext = [letter ^ xorVal for letter in encoded_string]
	return plaintext

if __name__ == "__main__":

	decoded = singlebyte_XOR_decode(encoded_string, 125)
	solved = [chr(element) for element in decoded]
	print("".join(solved))
