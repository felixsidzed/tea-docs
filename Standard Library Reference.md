# Standard Library Reference

## except

#### throw

```tea
@noreturn, @nonamespace
import func throw(string message) -> void;
```

**Parameters:**
- `message` - Error message

**Attributes:**
- `@noreturn` - This function never returns to the caller
- `@nonamespace` - This function is not in global scope

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

#### pcall

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

#### xpcall

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

---

## io

#### print

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

#### printf

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

#### readf

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

#### writef

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

#### readline

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

---

## math

#### abs

```tea
import func abs(int num) -> int;
```

Returns the absolute value of an integer.

**Parameters:**
- `num` - Integer value

**Returns:**
- Absolute value of `num`

**Example:**

```tea
using "io";
using "math";

public func main() -> int
	var result = math::abs(-42);
	io::printf("Absolute value: %d\n", result);
	
	return 0;
end
```

#### sqrt

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
	var result = math::sqrt(16);
	io::printf("Square root: %d\n", result);
	
	return 0;
end
```

#### sum

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

---

## memory

#### free

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

#### alloc

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
	
	// ...buffer
	memory::free(buffer);
	
	return 0;
end
```

#### copy

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

---

## string

#### len

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

#### eq

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

#### itoa

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
	var buffer: string;
	var result = string::itoa(42, buffer);
	
	io::printf("String: %s\n", result);
	return 0;
end
```

#### cat

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

#### sub

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

#### exit

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

#### time

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

#### sleep

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

#### spawn

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

#### join

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

#### close

```tea
import func close(void* thread) -> void;
```

Closes a thread handle.

**Parameters:**
- `thread` - Thread handle to close

**Note:** This does not terminate the thread or release it's resources.

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

#### exit

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

## Notes

### Memory Management

Many functions in the standard library return heap-allocated strings or buffers. These should be explicitly freed using `memory::free()` when no longer needed to avoid memory leaks.

### Thread Safety

The threading functions provide basic concurrent execution capabilities. Proper synchronization mechanisms should be implemented when accessing shared resources across threads.

### Error Handling

The `except` module provides exception handling. Use `except::pcall()` or `except::xpcall()` to catch exceptions gracefully from potentially failing operations.
