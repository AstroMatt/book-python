include_dirs = -I/usr/local/Cellar/python3/3.6.1/Frameworks/Python.framework/Versions/3.6/include/python3.6m/

ctypes:
	make clean
	gcc -fPIC -c -o hello-ctypes.o hello-ctypes.c $(include_dirs)
	gcc -shared hello-ctypes.o -o hello-ctypes.so

clean:
	rm -fr hello-ctypes.o
	rm -fr hello-ctypes.so

