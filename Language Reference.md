# Lexical Structure

### Keywords

```
using, public, func, var, return, if, do, else, end,
for, while, macro
```

### Operators

- **Arithmetic**: `+`, `-`, `*`, `/`, `%`
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Logical**: `&&`, `||`, `!`
- **Bitwise**: `&`, `|`, `^`, `~`, `<<`, `>>`
- **Pointer**: `*` (dereference), `&` (reference), `->` (arrow)
- **Cast**: `(type)`

### Delimiters

- `;` - Statement terminator
- `:` - Type annotation
- `()` - Function calls, grouping, conditionals
- `[]` - Array indexing
- `::` - Scope operator

### Comments

```tea
// noHello
```

### Examples

https://github.com/felixsidzed/tea/tree/main/playground/examples

### Hello World

```tea
using "io";

public func main() -> int
    io::print("Hello, World!\n");

    return 0;
end
```

### Fibonacci Sequence

```tea
using "io";

func fib(int n) -> int
    if (n <= 1) do
        return n;
    end

    return fib(n - 1) + fib(n - 2);
end

public func main() -> int
    for (var i = 0; i < 10; i += 1) do
        io::printf("fib(%d) = %d\n", i, fib(i));
    end

    return 0;
end
```

### Pointer Manipulation

```tea
using "io";

public func main() -> int
    var value: int = 100;
    var ptr: int* = &value;
    
    io::printf("value = %d\n", value);
    io::printf("address = %p\n", ptr);
    
    *ptr = 200;
    io::printf("modified value = %d\n", value);
    
    return 0;
end
```

### String Manipulation

```tea
using "io";
using "string";

public func main() -> int
    var str: string = "Hello, Tea!";
    var substr = string::sub(0, 5);
    
    io::printf("original: %s\n", str);
    io::printf("substr: %s\n", substr);
    
    return 0;
end
```

# Semantics

## Execution Model

Tea source code undergoes the following transformations:

1. Text -> Tokens (Tokenization/Lexer)
2. Tokens -> AST (parsing)
3. AST -> mid-level IR
4. Backend:
   - **LLVM**: MIR -> LLVM IR -> native machine code
   - **Luau** (experimental): MIR → Luau bytecode

**Program Entry**: Execution can begin at any function if an entry point is provided to the linker.

## Scoping Rules

**Module Scope**: Functions and macros declared at the top level are module-scoped

**Block Scope**: Variables declared in control flow blocks (if, for, while, do) and functions are scoped to them

```tea
if (condition) do
    var temp: int = 5;
	// ...
end
// temp is not accessible here
```

**Name Resolution**: Tea uses lexical scoping. Names are resolved in the following order:

1. Imported modules
2. Constants (true, false, null)
3. Functions
4. Globals
5. Function Parameters
6. Locals

### Binding Rules

**Variable Binding**: Variables are bound at declaration and cannot be redeclared in the same scope

```tea
var x: int = 10;
// var x: int = 20;  // ERR: redeclaration
x = 20;  // OK: reassignment
```

**Function Binding**: Functions are bound by name at module scope. The scope (`::`) operator accesses module members

```tea
using "io";
io::print("message");
```

**Method Binding**: Methods are bound to their objects at call time.

```tea
obj.method(...); // Standard method call
obj->method(...);   // Arrow call. Equivalent to `(*obj).method(...)'
```

### Evaluation Order

Tea evaluates expressions left-to-right with certain operators (`&&` and `||` using short-circuit evaluation)

**Operator Precedence** (highest to lowest):
10. Multiplicative: `*`, `/`, `%`
9. Additive: `+`, `-`
8. Shift: `<<`, `>>`
7. Relational: `<`, `>`, `<=`, `>=`
6. Equality: `==`, `!=`
5. Bitwise AND `&`
4. Bitwise XOR: `^`
3. Bitwise OR: `|`
2. Logical AND: `&&`
1. Logical OR: `||`

```tea
if (ptr != null && *ptr > 0) do
	// *ptr is only evaluated if ptr != null
end
```

Call arguments are evaluated left-to-right before the function call.

### Grammar

TODO
