# Standard Library Reference

## except

### throw

```tea
@noreturn, @nonamespace
import func throw(string message) -> void;
```

**Parameters:**
- `message` - Error message

**Attributes:**
- `@noreturn` - This function never returns to the caller
- `@nonamespace` - This function is in global scope

**Example:**

```tea
using "except";

public func main() -> int
	var value = -1;
	if (value < 0) do
		throw("value cannot be negative");
		// unreachable
	end
	
	return 0;
end
```

### pcall

```tea
import func pcall(void* f) -> string;
```

Calls a function in protected mode and catches any exceptions. Returns an error message if an exception occurs, or a null pointer on success.

**Parameters:**
- `f` - Function to call

**Returns:**
- Error message string if an exception occurred, null pointer otherwise

**Example:**

```tea
using "except";
using "io";

func risky() -> void
	throw("something went wrong");
end

public func main() -> int
	var err = except::pcall(risky); // or &risky
	if (err) do
		io::printf("Error caught: %s\n", err);
	end
	
	return 0;
end
```

### xpcall

```tea
import func xpcall(void* f, void* handler) -> bool;
```

Extended version of `pcall` that calls a custom error handler if an exception is thrown.

**Parameters:**
- `f` - Function to call
- `handler` - Error handler

**Returns:**
- `true` if execution succeeded, otherwise the return value of `handler`

**Example:**

```tea
using "io";
using "except";

func handler() -> bool
	io::print("error handler called\n");
	return true; // exception handled successfully
end

func risky() -> void
	throw("error occurred");
end

public func main() -> int
	var success = except::xpcall(risky, handler);
	if (!success) do
		io::print("operation failed\n");
	end
	
	return 0;
end
```

### assert

```tea
@nonamespace
import func assert(bool pred, string msg) -> void;
```

**Parameters:**
- `msg` - Error message

**Attributes:**
- `@nonamespace` - This function is in global scope

**Example:**

```tea
using "except";

public func main() -> int
	var a = 5;
	assert(a + 1 == 6, "a + 1 should equal to 6");
	
	return 0;
end
```

---

## io

### print

```tea
import func print(string message) -> void;
```

Prints a message to standard output.

**Parameters:**
- `message` - Message to print

**Example:**

```tea
using "io";

public func main() -> int
	io::print("Hello, World!\n");
	return 0;
end
```

### printf

```tea
import func printf(string fmt, ...) -> void;
```

Formatted print to standard output. Supports most C-style format specifiers.

**Parameters:**
- `fmt` - Format string
- `...` - Variable arguments matching format specifiers

**Example:**

```tea
using "io";

public func main() -> int
	var name: string = "Epstein";
	
	io::printf("Hello, %s!\n", name);
	return 0;
end
```

### readf

```tea
import func readf(string path) -> string;
```

Reads the entire contents of a file into a heap-allocated string.

**Parameters:**
- `path` - File path

**Returns:**
- File contents

**Note:** The returned string is on the heap and should be freed when no longer needed.

**Example:**

```tea
using "io";
using "memory";

public func main() -> int
	var content = io::readf("config.txt");
	io::printf("file content: %s\n", content);
	memory::free(content);
	
	return 0;
end
```

### writef

```tea
import func writef(string path, string data, int size) -> void;
```

Writes data to a file.

**Parameters:**
- `path` - File path
- `data` - Data to write
- `size` - Number of bytes to write

**Example:**

```tea
using "io";
using "string";

public func main() -> int
	var message: string = "Hello, File!";
	io::writef("output.txt", message, string::len(message));
	
	return 0;
end
```

### readline

```tea
import func readline() -> string;
```

Reads a line from standard input.

**Returns:**
- Heap-allocated string containing the input line

**Note:** The returned string is allocated on the heap and should be freed when no longer needed.

**Example:**

```tea
using "io";
using "memory";

public func main() -> int
	io::print("Enter your name: ");
	var name = io::readline();
	
	io::printf("Hello, %s!\n", name);
	memory::free(name);
	
	return 0;
end
```

### appendf

```tea
import func appendf(string path, string data, int size) -> void;
```

Appends data to a file.

**Parameters:**
- `path` - File path
- `data` - Data to append
- `size` - Number of bytes to append

**Example:**

```tea
using "io";
using "string";

public func main() -> int
	var message: string = "Hello, File!";
	io::appendf("output.txt", message, string::len(message));
	
	return 0;
end
```

### existsf

```tea
import func existsf(string path) -> bool;
```

Checks if a file exists.

**Parameters:**
- `path` - File path

### delf

```tea
import func delf(string path) -> bool;
```

Deletes a file.

**Parameters:**
- `path` - File path

### mkdir

```tea
import func mkdir(string path) -> bool;
```

Deletes a file.

**Parameters:**
- `path` - File path

### rmdir

```tea
import func rmdir(string path) -> bool;
```

Deletes an **empty** directory.

**Parameters:**
- `path` - Directory path

### tempdir

```tea
import func tempdir() -> string;
```

Creates a temporary directory.

**Returns:**
- Directory path

### tempfile

```tea
import func tempfile() -> string;
```

Creates a temporary file.

**Returns:**
- File path

---

## math

### abs

```tea
import func abs(int num) -> int;
```

Returns the absolute value of an integer.

**Parameters:**
- `num` - Integer value

**Returns:**
- Absolute value of `num`

### sqrt

```tea
import func sqrt(int num) -> int;
```

Computes the integer square root of a number.

**Parameters:**
- `num` - Non-negative integer

**Returns:**
- Integer square root of `num`

**Example:**

```tea
using "io";
using "math";

public func main() -> int
	var result = math::sqrt(81);
	io::printf("Square root: %d\n", result);
	
	return 0;
end
```

### sum

```tea
import func sum(int nargs, ...) -> int;
```

Computes the sum of a variable number of integers.

**Parameters:**
- `nargs` - Number of arguments to sum
- `...` - Variable number of integer arguments

**Returns:**
- Sum of all provided integers

**Example:**

```tea
using "io";
using "math";

public func main() -> int
	var total = math::sum(5, 10, 20, 30, 40, 50);
	io::printf("Sum: %d\n", total);
	
	return 0;
end
```

### max

```tea
import func max(int a, int b) -> int;
```

Returns the larger of two integers.

**Parameters:**

- `a` - First integer
- `b` - Second integer

**Returns:**

- The greater of `a` and `b`

---

### min

```tea
import func min(int a, int b) -> int;
```

Returns the smaller of two integers.

**Parameters:**

- `a` - First integer
- `b` - Second integer

**Returns:**

- The lesser of `a` and `b`

---

### clamp

```tea
import func clamp(int val, int min, int max) -> int;
```

Clamps a value to a given range.

**Parameters:**

- `val` - Value to clamp
- `min` - Minimum allowed value
- `max` - Maximum allowed value

**Returns:**

- `val` constrained to the range `[min, max]`

---

### pow

```tea
import func pow(int base, int exp) -> int;
```

Raises an integer to an integer power.

**Parameters:**

- `base` - Base value
- `exp` - Exponent (non-negative)

**Returns:**

- `base` raised to the power of `exp`

---

### srand

```tea
import func srand(unsigned int seed) -> void;
```

Seeds the random number generator.

**Parameters:**

- `seed` - Seed value

---

### random

```tea
import func random(int min, int max) -> int;
```

Generates a pseudo-random integer within a range.

**Parameters:**

- `min` - Minimum value (inclusive)
- `max` - Maximum value (inclusive)

**Returns:**

- Random integer in the range `[min, max]`

---

### ceil

```tea
import func ceil(double x) -> double;
```

Rounds a floating-point value up to the nearest integer.

**Parameters:**

- `x` - Double-precision value

**Returns:**

- Smallest integer value greater than or equal to `x`

---

### ceilf

```tea
import func ceilf(float x) -> float;
```

Rounds a floating-point value up to the nearest integer.

**Parameters:**

- `x` - Single-precision value

**Returns:**

- Smallest integer value greater than or equal to `x`

---

### floor

```tea
import func floor(double x) -> double;
```

Rounds a floating-point value down to the nearest integer.

**Parameters:**

- `x` - Double-precision value

**Returns:**

- Largest integer value less than or equal to `x`

---

### floorf

```tea
import func floorf(float x) -> float;
```

Rounds a floating-point value down to the nearest integer.

**Parameters:**

- `x` - Single-precision value

**Returns:**

- Largest integer value less than or equal to `x`

---

## memory

### free

```tea
import func free(void* buf) -> void;
```

Frees previously allocated memory.

**Parameters:**
- `buf` - Pointer to memory to free

**Example:**

```tea
using "memory";

public func main() -> int
	var buffer = memory::alloc(100);
	// ...use buffer
	memory::free(buffer);
	
	return 0;
end
```

### alloc

```tea
import func alloc(long size) -> void*;
```

Allocates a block of memory on the heap.

**Parameters:**
- `size` - Number of bytes to allocate

**Returns:**
- Pointer to allocated memory

**Example:**

```tea
using "memory";
using "io";

public func main() -> int
	var buffer: int* = memory::alloc(10 * 4);
	
	if (!buffer) do
		io::print("Allocation failed\n");
		return 1;
	end
	
	// ...use buffer
	memory::free(buffer);
	
	return 0;
end
```

### copy

```tea
import func copy(void* dest, const void* src, unsigned int n) -> void*;
```

Copies `n` bytes from source to destination memory.

**Parameters:**
- `dest` - Destination pointer
- `src` - Source pointer
- `n` - Number of bytes to copy

**Returns:**
- Pointer to destination

**Example:**

```tea
using "memory";
using "io";

public func main() -> int
	var src: int = 42;
	var dest: int = 0;
	
	memory::copy(&dest, &src, 4);
	io::printf("Copied value: %d\n", dest);
	
	return 0;
end
```

### realloc

```tea
import func realloc(void* ptr, long nsize) -> void*;
```

Reallocates a block of memory to a new size.

**Parameters:**
- `ptr` - Pointer to previously allocated memory (or null)
- `nsize` - New size in bytes

**Returns:**
- Pointer to reallocated memory

**Example:**

```tea
using "memory";
using "io";

public func main() -> int
	var buffer: int* = memory::alloc(10 * 4);
	
	// ...use buffer

	// resize to hold 20 integers
	buffer = memory::realloc(buffer, 20 * 4);

	// ...use buffer
	
	memory::free(buffer);
	return 0;
end
```

### set

```tea
import func set(void* dest, unsigned char src, unsigned int n) -> void*;
```

Sets `n` bytes of memory to a specified value.

**Parameters:**
- `dest` - Destination pointer
- `src` - Byte value to set
- `n` - Number of bytes to set

**Returns:**
- Pointer to destination

**Example:**

```tea
using "memory";
using "io";

public func main() -> int
	var buffer: char[10];
	memory::set(buffer, 0, 10);  // Zero out buffer
	
	return 0;
end
```

### cmp

```tea
import func cmp(const void* p1, const void* p2, unsigned int n) -> int;
```

Compares two memory regions byte by byte.

**Parameters:**
- `p1` - First memory pointer
- `p2` - Second memory pointer
- `n` - Number of bytes to compare

**Returns:**
- 0 if regions are equal, non-zero otherwise

**Example:**

```tea
using "memory";
using "io";

public func main() -> int
	var a: int = 42;
	var b: int = 42;
	
	if (memory::cmp(&a, &b, 4) == 0) do
		io::print("values are equal\n");
	end
	
	return 0;
end
```

---

## string

### len

```tea
import func len(string str) -> int;
```

Returns the length of a string.

**Parameters:**
- `str` - String to measure

**Returns:**
- Length of the string in bytes

**Example:**

```tea
using "io";
using "string";

public func main() -> int
	var text: string  = "Hello";
	var length = string::len(text);
	
	io::printf("Length: %d\n", length);
	return 0;
end
```

### eq

```tea
import func eq(string s1, string s2) -> bool;
```

Compares two strings for equality.

**Parameters:**
- `s1` - First string
- `s2` - Second string

**Returns:**
- `true` if strings are equal, `false` otherwise

**Example:**

```tea
using "io";
using "string";

public func main() -> int
	var str1: string = "hello";
	var str2: string = "hello";
	
	if (string::eq(str1, str2)) do
		io::print("Strings are equal\n");
	end
	
	return 0;
end
```

### itoa

```tea
import func itoa(int num, string buffer) -> string;
```

Converts an integer to a string representation.

**Parameters:**
- `num` - Integer to convert
- `buffer` - Buffer to store the result

**Returns:**
- String representation of the integer

**Example:**

```tea
using "io";
using "string";

public func main() -> int
	var buffer: char[32];
	var result = string::itoa(42, buffer);
	
	io::printf("String: %s\n", result);
	return 0;
end
```

### cat

```tea
import func cat(int nargs, ...) -> string;
```

Concatenates multiple strings into a single heap-allocated string.

**Parameters:**
- `nargs` - Number of strings to concatenate
- `...` - Variable number of string arguments

**Returns:**
- Heap-allocated concatenated string

**Note:** The returned string is allocated on the heap and should be freed when no longer needed.

**Example:**

```tea
using "io";
using "string";
using "memory";

public func main() -> int
	var result = string::cat(3, "Hello", ", ", "World!");
	io::printf("%s\n", result);
	memory::free(result);
	
	return 0;
end
```

### sub

```tea
import func sub(string str, int i, int j) -> string;
```

Extracts a substring from a string.

**Parameters:**
- `str` - Source string
- `i` - Starting index (inclusive)
- `j` - Ending index (exclusive)

**Returns:**
- Heap-allocated substring

**Note:** The returned string is allocated on the heap and should be freed when no longer needed.

**Example:**

```tea
using "io";
using "string";
using "memory";

public func main() -> int
	var text: string = "Hello, Tea!";
	var substr = string::sub(text, 0, 5);
	
	io::printf("substr: %s\n", substr);
	memory::free(substr);
	
	return 0;
end
```

---

## sys

### exit

```tea
@noreturn
import func exit(int exitCode) -> void;
```

Terminates the program with the specified exit code.

**Parameters:**
- `exitCode` - Exit status code

**Attributes:**
- `@noreturn` - This function never returns to the caller

**Example:**

```tea
using "sys";
using "io";

public func main() -> int
	io::print("Exiting program...\n");
	sys::exit(0);
end
```

### time

```tea
import func time() -> long;
```

Returns the current system time in milliseconds since epoch.

**Returns:**
- Current time as a 64-bit integer

**Example:**

```tea
using "io";
using "sys";

public func main() -> int
	var timestamp = sys::time();
	io::printf("Current time: %ld\n", timestamp);
	
	return 0;
end
```

### sleep

```tea
import func sleep(int milliseconds) -> void;
```

Suspends program execution for the specified duration.

**Parameters:**
- `milliseconds` - Number of milliseconds to sleep

**Example:**

```tea
using "io";
using "sys";

public func main() -> int
	io::print("Waiting 1 second...\n");
	sys::sleep(1000);
	io::print("Done!\n");
	
	return 0;
end
```

---

## thread

### spawn

```tea
import func spawn(void* f) -> void*;
```

Creates and starts a new thread executing the given function.

**Parameters:**
- `f` - Function pointer to execute in the new thread

**Returns:**
- Thread handle for the created thread

**Example:**

```tea
using "io";
using "thread";

func worker() -> void
	io::print("Worker thread running\n");
end

public func main() -> int
	var t = thread::spawn(worker);
	thread::join(t);
	thread::close(t);
	
	return 0;
end
```

### join

```tea
import func join(void* thread) -> void;
```

Waits for the specified thread to complete execution.

**Parameters:**
- `thread` - Thread handle to wait for

**Example:**

```tea
using "thread";
using "io";

func task() -> void
	io::print("Task completed\n");
end

public func main() -> int
	var t = thread::spawn(task);
	io::print("waiting for thread...\n");
	thread::join(t);
	thread::close(t);
	
	return 0;
end
```

### close

```tea
import func close(void* thread) -> void;
```

Closes a thread handle.

**Parameters:**
- `thread` - Thread handle to close

**Note:** This does **not** terminate the thread or release it's resources.

**Example:**

```tea
using "thread";

public func main() -> int
	var t = thread::spawn(some_function);
	thread::join(t);
	thread::close(t);
	
	return 0;
end
```

### exit

```tea
@noreturn
import func exit(int exitCode) -> void;
```

Terminates the current thread with the specified exit code.

**Parameters:**
- `exitCode` - Exit status code for the thread

**Attributes:**
- `@noreturn` - This function never returns to the caller

**Example:**

```tea
using "thread";
using "io";

func worker() -> void
	io::print("Worker exiting\n");
	thread::exit(0);
end

public func main() -> int
	var t = thread::spawn(&worker);
	thread::join(t);
	thread::close(t);
	
	return 0;
end
```

---

## mutex

### new

```tea
import func new() -> void*;
```

Creates a new mutex.

**Returns:**
- Mutex handle

**Example:**

```tea
using "io";
using "mutex";

public func main() -> int
	var mtx = mutex::new();
	
	mutex::lock(mtx);
	io::print("critical section\n");
	mutex::unlock(mtx);
	
	return 0;
end
```

### lock

```tea
import func lock(void* mtx) -> void;
```

Locks a mutex, blocking until the lock is acquired.

**Parameters:**
- `mtx` - Mutex handle

**Example:**

```tea
using "io";
using "mutex";

private var mtx: void*;

func worker() -> void
	mutex::lock(mtx);
	io::print("thread has lock\n");
	mutex::unlock(mtx);
end

public func main() -> int
	mtx = mutex::new();
	// ...use mutex

	return 0;
end
```

### unlock

```tea
import func unlock(void* mtx) -> void;
```

Unlocks a mutex.

**Parameters:**
- `mtx` - Mutex handle

### cvnew

```tea
import func cvnew() -> void*;
```

Creates a new condition variable.

**Returns:**
- Condition variable handle

**Example:**

```tea
using "mutex";

public func main() -> int
	var cv = mutex::cvnew();
	var mtx = mutex::new();
	
	// ...use condition variable

	return 0;
end
```

### wait

```tea
import func wait(void* cv, void* mtx) -> void;
```

Waits on a condition variable, atomically releasing the mutex and blocking until signaled.

**Parameters:**
- `cv` - Condition variable handle
- `mtx` - Associated mutex handle

**Example:**

```tea
using "mutex";
using "io";

var cv: void*;
var mtx: void*;

func waiter() -> void
	mutex::lock(mtx);

	io::print("waiting for signal...\n");
	mutex::wait(cv, mtx);
	io::print("signal received!\n");

	mutex::unlock(mtx);
end

public func main() -> int
	cv = mutex::cvnew();
	mtx = mutex::new();

	// ...spawn waiter thread
	return 0;
end
```

### signal

```tea
import func signal(void* cv) -> void;
```

Signals one thread waiting on a condition variable.

**Parameters:**
- `cv` - Condition variable handle

**Example:**

```tea
using "mutex";

public func main() -> int
	var cv = mutex::cvnew();
	mutex::signal(cv);
	
	return 0;
end
```

### broadcast

```tea
import func broadcast(void* cv) -> void;
```

Signals all threads waiting on a condition variable.

**Parameters:**
- `cv` - Condition variable handle

**Example:**

```tea
using "mutex";

public func main() -> int
	var cv = mutex::cvnew();
	
	mutex::broadcast(cv);
	
	return 0;
end
```

---

## socket

### connect

```tea
import func connect(const char* host, unsigned short port) -> void*;
```

Connects to a remote host.

**Parameters:**
- `host` - Hostname or IP address
- `port` - Port number

**Returns:**
- Socket handle, or null on failure

**Example:**

```tea
using "io";
using "socket";

public func main() -> int
	var sock = socket::connect("example.com", 80);

	if (!sock) do
		io::print("connection failed\n");
		return 1;
	end
	
	// ...use socket
	socket::close(sock);
	
	return 0;
end
```

### accept

```tea
import func accept(void* sock) -> void*;
```

Accepts an incoming connection on a listening socket.

**Parameters:**
- `sock` - Listening socket handle

**Returns:**
- New socket handle for the accepted connection

**Example:**

```tea
using "io";
using "socket";

public func main() -> int
	var server = socket::listen(8080);
	io::print("waiting for connection...\n");
	
	var client = socket::accept(server);
	io::print("client connected!\n");
	
	socket::close(client);
	socket::close(server);
	
	return 0;
end
```

### listen

```tea
import func listen(unsigned short port) -> void*;
```

Creates a listening socket on the specified port.

**Parameters:**
- `port` - Port number to listen on

**Returns:**
- Listening socket handle, or null on failure

**Example:**

```tea
using "socket";
using "io";

public func main() -> int
	var server = socket::listen(8080);
	
	if (!server) do
		io::print("failed to create server\n");
		return 1;
	end
	
	io::print("server listening on port 8080\n");
	
	// ...accept connections
	socket::close(server);
	
	return 0;
end
```

### recv

```tea
import func recv(void* sock, string buf, int size) -> int;
```

Receives data from a socket.

**Parameters:**
- `sock` - Socket handle
- `buf` - Buffer to store received data
- `size` - Maximum number of bytes to receive

**Returns:**
- Number of bytes received, or -1 on error

**Example:**

```tea
using "socket";
using "io";

public func main() -> int
	var sock = socket::connect("example.com", 80);
	var buffer: char[256];
	
	var bytesRead = socket::recv(sock, buffer, 256);
	buffer[bytesRead] = '\0';

	io::printf("received %d bytes: %s\n", bytesRead, buffer);
	
	socket::close(sock);
	return 0;
end
```

### send

```tea
import func send(void* sock, string data, int size) -> int;
```

Sends data through a socket.

**Parameters:**
- `sock` - Socket handle
- `data` - Data to send
- `size` - Number of bytes to send

**Returns:**
- Number of bytes sent, or -1 on error

**Example:**

```tea
using "io";
using "socket";
using "string";

public func main() -> int
	var sock = socket::connect("example.com", 80);
	var message: string = "GET / HTTP/1.1\r\n\r\n";
	
	var bytesSent = socket::send(sock, message, string::len(message));
	io::printf("sent %d bytes\n", bytesSent);
	
	socket::close(sock);
	return 0;
end
```

### close

```tea
import func close(void* sock) -> void;
```

Closes a socket connection.

**Parameters:**
- `sock` - Socket handle to close

**Example:**

```tea
using "socket";

public func main() -> int
	var sock = socket::connect("example.com", 80);
	
	// ...use socket
	
	socket::close(sock);
	return 0;
end
```

---

## Notes

### Memory Management

Many functions in the standard library return heap-allocated strings or buffers. These should be explicitly freed using `memory::free()` when no longer needed to avoid memory leaks.

### Thread Safety

The threading functions provide basic concurrent execution capabilities. Proper synchronization mechanisms should be implemented when accessing shared resources across threads.

### Error Handling

The `except` module provides exception handling. Use `except::pcall()` or `except::xpcall()` to catch exceptions gracefully from potentially failing operations.
