**Tea** (pronounced /teə/) is a multi-backend, general-purpose programming language

## Target Users

shi idk anyone that wants to ig
originally i made ts js for myself

## Use Cases

Anything from systems programming & game development to educational environments

## Core Philosophy

Simplicity with power. This manifests in:

- **Explicit over Implicit**: Operations like dereferencing and type casting are clearly visible
- **Familiar Syntax**: Drawing from popular languages reduces the learning curve
- **No Hidden Costs**: Performance implications of operations are predictable
- **Direct Hardware Access**: Pointers and manual memory management available when needed

## Trade-offs

1. Manual memory management for performance and flexibility
2. Static typing

## Paradigms

Tea is primarily procedural, with functions as first-class organizational units.

```tea
public func distance(double x1, double y1, double x2, double y2) -> double
    var dx = x2 - x1;
    var dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
end
```

## Type System

**Static Typing**: All variables have types known at compile-time

```tea
var count: int = 0;
var name: string = "John";
var ratio: double = 3.14159;
```

**Type Inference**: The compiler can deduce types from initializers

```tea
var x = 42;			// inferred as int
var y = 3.14f;		// inferred as float
var z = "hello";	// inferred as string
```

**Strong Typing**: Type conversions must be explicit via casting

```tea
var i: int = 42;
var d: double = (double)i;  // explicit cast required
```

**Primitive Types**:
- `void`: No value
- `bool`: Boolean type
- `char`: 8-bit integer
- `short`: 16-bit integer
- `int`: 32-bit integer
- `long`: 64-bit integer
- `float`: 32-bit single-precision floating-point
- `double`: 64-bit double-precision floating-point
- `string`: QoL/readability type. Equivalent to `char*`

**Composite Types**:
- Pointers: `type*` (e.g., `int*`, `double*`)
- Arrays: `type[size]` (e.g. `bool[3]`, `string[5]`)
- Function: `func(returnType)(...params)` (e.g. `func(int)(int, int)`, `func(void)(const char*, ...)`)
- Classes:
```tea
class Vector2
	public var x: float;
	public var y: float;

	Vector2(float x, float y)
		this->x = x;
		this->y = y;
	end
end
```

## Memory Model

Tea uses explicit pointers and manual allocation

```tea
var value: double = 42.42;
var ptr: double* = &value;	// Reference (addressof) operator
var deref = *ptr;			// Dereference operator
```

Direct manipulation of memory addresses is supported.

```tea
var arr: int* = allocate_array(10);
var second: int* = arr + 1;
```

## Error Handling

Tea provides error handling through the standard library:

```tea
using "io";
using "str";
using "except";

public func test() -> void
	// except::throw has the '@nonamespace' attribute
	throw("an exception");
end

// returns whether the exception was handled
public func handler(string error) -> bool
	if (str::eq(error, "an exception")) do
		io::print("exception caught!\n");
		return true;
	end
	return false;
end

public func main()
	var handled = core::xpcall(test, handler);
	if (!handled) do
		io::print("unhandled exception\n");
		return 1;
	end

	return 0;
end
```

## Concurrency Model

Tea provides multi-threading through the standard library:

```tea
using "io";
using "thread";

@threadlocal
public var boogie: int = 1;

public func foo() -> void
	io::printf("(foo) boogie before = %d\n", boogie);
	boogie = 2;
	io::printf("(foo) boogie after = %d\n", boogie);
end

public func main() -> int
	io::printf("(main) boogie before = %d\n", boogie);
	thread::spawn(foo);
	io::printf("(main) boogie after = %d\n", boogie);

	return 0;
end
```
