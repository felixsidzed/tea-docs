Standard Library Reference
==========================

Detailed documentation on the functions of the Tea standard library.

IO
--
The `IO` module provides basic input and output functionalities, including printing to standard output, reading from standard input, and file I/O operations.

.. currentmodule:: io

.. function:: print(string message) -> bool

	Writes the given string to standard output without any formatting.

	:param message: The text to be printed.
	:returns: ``true`` if the operation succeeded, otherwise ``false``.

.. function:: printf(string fmt, ...) -> bool

	Prints a formatted string to standard output. Similar to `printf` in C.

	:param fmt: The format string (e.g., ``"Hello, %s!"``).
	:param ...: Arguments to be substituted into the format string.
	:returns: ``true`` if the operation succeeded, otherwise ``false``.

.. function:: flush() -> bool

	Flushes the standard output buffer, ensuring all output is written immediately.

	:returns: ``true`` if the buffer was successfully flushed.

.. function:: readline() -> string

	Reads a single line of input from standard input, up to the newline character.

	:returns: The input line as a string.

	.. tip::

		It is recommended to free the result string using `mem::free`

		.. dropdown:: Why?

			Internally, io::readline uses HeapAlloc and HeapRealloc to ensure memory safety.
			
			These functions allocate memory on the heap that is managed separately from the stack. 
			If you do not free the memory using `mem::free`, it can lead to memory leaks—where allocated memory is never released back to the system. 
			Over time, especially in long-running programs or repeated allocations (e.g., in loops or user input), this can exhaust system memory and degrade performance or even crash the application.

.. function:: writef(string path, string content) -> bool

	Writes the specified content to a file at the given path. Overwrites existing content.

	:param path: The file path.
	:param content: The content to write to the file.
	:returns: ``true`` if the write was successful, otherwise ``false``.

.. function:: readf(path: string) -> string

	Reads the entire contents of a file at the specified path.

	:param path: The file path to read from.
	:returns: Contents of the file as a string.

	.. tip::

		It is recommended to free the result string using `mem::free`

		.. dropdown:: Why?

			Internally, io::readf uses HeapAlloc to ensure memory safety.
			
			These functions allocate memory on the heap that is managed separately from the stack. 
			If you do not free the memory using `mem::free`, it can lead to memory leaks—where allocated memory is never released back to the system. 
			Over time, especially in long-running programs or repeated allocations (e.g., in loops or user input), this can exhaust system memory and degrade performance or even crash the application.

Math
----

The `Math` module provides basic mathematical operations such as absolute value, square root calculation, and summation.

.. currentmodule:: math

.. function:: abs(int n) -> int

   Returns the absolute value of the given integer.

   :param n: The integer whose absolute value is to be computed.
   :returns: The absolute value of the input integer.

.. function:: sqrt(int n) -> int

   Returns the square root of the given integer.

   :param value: The integer to compute the square root of.
   :returns: The square root of the input integer.

.. function:: sum(int count, int...) -> int

   Computes the sum of the given integers.

   :param count: The number of variadic arguments passed.
   :param values: The integers to be summed.
   :returns: The sum of the integers.

String
------
The `String` module provides basic string operations such as length calculation, substring extraction and string concatenation

.. currentmodule:: str

.. function:: len(string str) -> int

	Returns the length of a null-terminated string.

	:param str: The null-terminated string.
	:returns: The length of the string.

.. function:: itoa(int num) -> string

	Converts the number *num* into a string.

	:param num: The number to stringify.
	:returns: The number as a string.

.. function:: sub(string str, int start, int end) -> string

    Extracts a substring from the given string.

    :param str: The string to extract the substring from.
    :param start: The starting index (inclusive) from where to begin extraction.
    :param end: The ending index (exclusive) up to which the substring will be extracted.
    :returns: The extracted substring between the start and end indices.

.. function:: eq(string lhs, string rhs) -> bool

    Compares two strings for equality.

    :param lhs: The first string to compare.
    :param rhs: The second string to compare.
    :returns: ``true`` if the strings are equal, otherwise ``false``.

.. function:: cat(int count, ...) -> string

	Concatenates the provided strings into one.

	:param count: The amount of strings to concatenate.
	:param ...: The strings to concatenate.
	:returns: The concatenated string.

	.. tip::

		It is recommended to free the result string using `mem::free`

		.. dropdown:: Why?

			Internally, str::cat uses HeapAlloc to ensure memory safety.
			
			These functions allocate memory on the heap that is managed separately from the stack. 
			If you do not free the memory using `mem::free`, it can lead to memory leaks—where allocated memory is never released back to the system. 
			Over time, especially in long-running programs or repeated allocations (e.g., in loops or user input), this can exhaust system memory and degrade performance or even crash the application.

Memory
------

The `Memory` module provides access to basic memory operations such as free.

.. currentmodule:: mem

.. function:: free(void* block) -> bool

	Frees *block* from the memory heap. Similar to `free` in C.

	:param block: The memory block to free.
	:returns: Whether the HeapFree succeeded.

System
------

The `System` module provides access to basic system operations such as exit, time and sleep.

.. currentmodule:: sys

.. function:: exit(int code) -> noreturn

	Exits from the current process with an exit code.

	:param code: The exit code.

.. function:: time() -> long

	Returns the current system time as a UNIX timestamp.

	:returns: The system time.

.. function:: sleep(int ms) -> void

	Halts the current thread's execution for `ms` milliseconds

	:param ms: The amount of milliseconds to sleep for.
