#!/usr/bin/env python3

import ctypes

lib = ctypes.CDLL('hello-ctypes.so')

print('-' * 30)

name = 'José Jiménez'
buffer = ctypes.create_string_buffer(name.encode('ASCII'))
lib.say_hello.argtypes = [ctypes.c_char_p]
greeting = lib.say_hello(buffer)
print(greeting)

print('-' * 30)

print('Factorial:')
print(lib.factorial(16))
print(lib.factorial(17))

print('-' * 30)

time = lib.what_time()
print(time)

print('-' * 30)

lib = ctypes.CDLL('/usr/lib/libc.dylib')
lib.printf("I'm C printf() function called from Python")

