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

		It is important to free the result using `mem::free`

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

		It is important to free the result using `mem::free`

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

		It is important to free the result using `mem::free`

		.. dropdown:: Why?

			Internally, str::cat uses HeapAlloc to ensure memory safety.
			
			These functions allocate memory on the heap that is managed separately from the stack. 
			If you do not free the memory using `mem::free`, it can lead to memory leaks—where allocated memory is never released back to the system. 
			Over time, especially in long-running programs or repeated allocations (e.g., in loops or user input), this can exhaust system memory and degrade performance or even crash the application.

Memory
------

The `Memory` module provides access to basic memory operations such as heap allocation and free.

.. currentmodule:: mem

.. function:: free(void* block) -> bool

	Frees *block* from the memory heap. Similar to `free` in C.

	:param block: The memory block to free.
	:returns: Whether the HeapFree succeeded.

.. function:: alloc(int size) -> void*

	Allocates *size* bytes in the memory heap and returns a pointer to them. Similar to `malloc` in C.

	:param size: The amount of bytes to allocate.
	:returns: The pointer to the allocated space.

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

Thread
------

The `Thread` module provides access to basic multithreading operations such as creating a thread and waiting for it to complete

.. currentmodule:: thread

.. function:: create(func f) -> void*

	Creates a new thread to execute the specified function.

	:param f: A function to run on the created thread. The function must take 0 arguments and return ``void``
	:returns: A pointer to the newly created thread.

.. function:: join(void* thread) -> void

	Blocks the calling thread until the specified thread completes.

	:param thread: The thread to wait for.

Net
---

The `Net` module provides access to basic socket operations such as creating a socket and sending data.

.. currentmodule:: net

.. function:: connect(string host, int port) -> void*

   Creates a **client** TCP socket and connects it to the specified IP address.

   :param host: The IP address to connect to.
   :param port: The port to connect to.
   :returns: The created socket.

.. function:: listen(int port) -> void*

   Creates a **server** TCP socket and listens for incoming connections on the specified port.

   :param port: The port to listen on.
   :returns: The created server socket.

.. function:: accept(void* socket) -> void*

   Accepts an incoming connection from a client.

   :param socket: The server socket instance to accept connections from.
   :returns: A socket representing the connected client.

.. function:: send(void* socket, string data) -> void

   Sends data over the specified socket.

   :param socket: The socket through which data will be sent.
   :param data: The data to send.

.. function:: recv(void* socket, int size) -> str

   Receives data from the specified socket.

   :param socket: The socket from which to receive data.
   :param size: The maximum amount of data to receive (in bytes).
   :returns: The received data.

   .. tip::

      It is important to free the result using `mem::free`.

      .. dropdown:: Why?

         Internally, `net::recv` uses `HeapAlloc` to allocate memory for the received data.
         
         This means that the allocated memory is managed separately from the stack. If you do not free the memory using `mem::free`, it may lead to memory leaks—where allocated memory is not returned to the system. Over time, especially in long-running programs or during repeated allocations (e.g., in loops or with user input), this can exhaust system memory, degrade performance, and even cause the application to crash.

.. function:: close(void* socket) -> void

   Closes the specified socket.

   :param socket: The socket to close.

.. function:: settimeout(void* socket, int timeout) -> void

   Sets the timeout duration for the specified socket.

   :param socket: The socket instance.
   :param timeout: The timeout duration in seconds.

Core
----

The `Core` module provides access to basic core operations such as exceptions.

.. currentmodule:: core

.. function:: throw(string message) -> noreturn

	Throws an error with the specified message. This function never returns, as it interrupts normal execution and signals an exception.

	:param message: The error message.
	:throws: An exception with the given message.

.. function:: pcall(void* f) -> string

	Calls the specified function in protected mode.
	If the function completes successfully, `null` is returned.
	If an exception is thrown, the error message is returned instead.

	:param f: The function to call.
	:returns: The error message or `null`.

.. function:: xpcall(void* f, void* handler) -> bool

	Calls the specified function in protected mode.
	If an exception is thrown during the execution of *f*, the optional *handler* is invoked with the error message.
	The return value indicates whether the exception was successfully handled.
	If *handler* is not provided (i.e., is `null`), `xpcall` will return ``true`` if the function succeeded, ``false`` otherwise.

	:param f: The function to call. (``func f() -> void``)
	:param handler: (optional) The error handler. (``func handler(string error) -> bool``)
	:returns: Whether the exception was handled.
