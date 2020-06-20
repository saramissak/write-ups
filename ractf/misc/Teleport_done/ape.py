#!/usr/bin/python3

from pwn import *

host, port = '88.198.219.20', 29053

s = remote(host, port)

i = 0
coords = 7
while coords < 10000000000000:
	s.sendline(str(coords)+','+str(coords))
	coords += 7
	try:
		prompt = s.recvuntil('Enter next position(maximum distance of 10):')
		pos = prompt.decode("utf-8").split('\n')[0]
		print(pos)
	except Exception as e:
		print(s.recvline())
		break;


s.close()