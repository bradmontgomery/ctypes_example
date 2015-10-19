all:
	# compile the c code for a static lib
	gcc -c algorithms.c -o algorithms.o
	# create the static library with archiver
	ar rcs libalgo.a algorithms.o
	# Compile, linked against the static lib
	gcc -Bstatic main.c -L. -lalgo -o main_static
	# Compile the C code for a dynamic lib, OSX-specific
	gcc -dynamiclib algorithms.c -o libalgo.1.dylib -current_version 1.0 -compatibility_version 1.0
	# Compile, linked against the dynamic lib
	gcc -Wall -g main.c -o main_dynamic libalgo.1.dylib

clean:
	rm libalgo.a libalgo.1.dylib main_dynamic main_static
	rm -rf main_dynamic.dSYM
