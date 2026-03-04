#!/usr/bin/env python3

hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

with open('./encfile', 'rb') as f:
    enc_s = f.read()

enc_list = [int(enc_s[i:i+2], 16) for i in range(0, len(enc_s), 2)]
plain_list = list(range(len(enc_list)))

for i in range(len(enc_list)):
    plain_list[i] = (enc_list[i] + 128) % 256

plain_b = bytes(plain_list)

with open('./flag.png', 'wb') as f:
    f.write(plain_b)
