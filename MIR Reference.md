# Mid-level IR Reference

Tea's Mid-level Intermediate Representation (MIR) is a low-level, typed intermediate representation used in the Tea compiler. It provides a structured way to represent programs before code generation, similar to LLVM IR but tailored for Tea's needs.

## Type System

MIR is strongly typed, with every value having an associated type. See [Type System](https://fentanyl-llc.gitbook.io/tea/#type-system)

## Values

All entities in MIR are represented as values. There are several kinds of values:

### Constants

#### Number Constants
Numeric literals representing integer or floating-point values. The bitwidth is determined by the type:
- `bool`: 1 bit
- `char`: 8 bits
- `short`: 16 bits
- `int`, `float`: 32 bits
- `long`, `double`: 64 bits

#### String Constants
Null-terminated character arrays stored as constants

#### Array Constants
Constant arrays containing multiple same-type values

#### Pointer Constants
Constant pointer values

### Functions

Functions are callable values with a signature (function type), parameter list, and body consisting of basic blocks. Functions have:
- **Storage class**: Controls visibility (public, private)
- **Calling convention**: Specifies how arguments are passed
- **Attributes**: Metadata like `inline`, `noreturn`, etc.

Function parameters can be referenced within function bodies by their name following a `%` (value) prefix.

```
public func foo(int %a) -> int
entry:
	%1 = add int %a, int 5
	ret %1
end
```

### Globals

Global variables with optional initializers. Like functions, they have storage classes and attributes.

```
public var @myInt: int = 67
private var @uninitialized: float
```

## Instructions

Instructions are the fundamental operations in MIR. Each instruction has an opcode, operands, and optionally produces a result value.

### Arithmetic

#### `add`
Adds two numeric values.
```
%result = add %lhs, %rhs
```

<details>
	<summary>Maps to</summary>

	LLVM: ```llvm
	%result = add %lhs, %rhs
	```
	or
	```
	%result = fadd %lhs, %rhs
	```
	if lhs type is floating-point
</details>

#### `sub`
Subtracts the second operand from the first.
```
%result = sub %lhs, %rhs
```

#### `mul`
Multiplies two numeric values.
```
%result = mul %lhs, %rhs
```

#### `div`
Divides the first operand by the second. Signedness is determined by the first operand's type.
```
%result = div %lhs, %rhs
```

#### `mod`
Computes the remainder of division.
```
%result = mod %lhs, %rhs
```

### Bitwise Operations

#### `not`
Performs bitwise negation.
```
%result = not %operand
```

#### `and`
Performs bitwise AND.
```
%result = and %lhs, %rhs
```

#### `or`
Performs bitwise OR.
```
%result = or %lhs, %rhs
```

#### `xor`
Performs bitwise exclusive OR.
```
%result = xor %lhs, %rhs
```

#### `shl`
Shifts bits left.
```
%result = shl %value, %amount
```

#### `shr`
Shifts bits right.
```
%result = shr %value, %amount
```

### Comparison

#### `icmp`
Integer comparison with a predicate:
- `eq`: equal
- `neq`: not equal
- `sgt`: signed greater than
- `ugt`: unsigned greater than
- `sge`: signed greater than or equal
- `uge`: unsigned greater than or equal
- `slt`: signed less than
- `ult`: unsigned less than
- `sle`: signed less than or equal
- `ule`: unsigned less than or equal

```
%result = icmp eq %lhs, %rhs
```

#### `fcmp`
Floating-point comparison with a predicate:
- `oeq`: ordered equal
- `oneq`: ordered not equal
- `ogt`: ordered greater than
- `oge`: ordered greater than or equal
- `olt`: ordered less than
- `ole`: ordered less than or equal
- `true`: always `true`
- `false`: always `false`

```
%result = fcmp oeq %lhs, %rhs
```

### Memory Operations

#### `load`
Reads a value from memory.
```
%result = load %ptr
```
Supports a volatile flag for preventing optimization.
```
%result = volatile load %ptr
```

#### `store`
Writes a value to memory.
```
store %pointer, %value
```
Supports a volatile flag for preventing optimization.
```
volatile store %pointer, %value
```

#### `alloca`
Allocates stack memory for a value of the specified type.
```
%result = alloca type
```

#### `gep`
Computes the address of an element within an aggregate type (array or struct).
```
%result = gep %pointer, %index
%result = gep %pointer, %index1, %index2, ...
```

### Control Flow

#### `br`
Unconditional branch to a basic block.
```
br %target
```

#### `cbr`
Conditional branch based on a boolean predicate.
```
cbr %pred, %true_block, %false_block
```

#### `ret`
Returns from the current function.
```
ret %value
ret void
```

#### `phi`
PHI node for SSA form, merging values from different predecessor blocks.
```
%result = phi [%value1, %block1], [%value2, %block2], ...
```

### Function Operations

#### `call`
Invokes a function with arguments.
```
%result = call %function(%arg1, %arg2, ...)
```

### Miscellaneous

#### `nop`
No operation; does nothing.
```
nop
```

#### `cast`
Converts a value from one type to another.
```
%result = cast %value to type
```

#### `unreachable`
Indicates that this code path should never be reached.
```
unreachable
```

## Basic Blocks

A basic block is a sequence of instructions with a single entry point (the first instruction) and a single exit point (a terminator instruction). Basic blocks are the nodes in a function's control flow graph.

See [Functions](https://fentanyl-llc.gitbook.io/tea/mir-reference#functions)

### Terminators

Every basic block must end with a terminator instruction:
- `br`: Unconditional branch
- `cbr`: Conditional branch
- `ret`: Return from function
- `unreachable`: Mark unreachable code

See [Instructions](https://fentanyl-llc.gitbook.io/tea/mir-reference#instructions)

## Modules

A module is the top-level container for MIR code. It contains:
- [Global variables](https://fentanyl-llc.gitbook.io/tea/mir-reference#globals)
- [Function definitions](https://fentanyl-llc.gitbook.io/tea/mir-reference#functions)
- Source information
- Data layout specification
- Target triple

### Data Layout

Specifies target-specific information:
- **Endianness**: Byte order (little-endian, big-endian)
- **Max native bytes**: Maximum native integer size in bytes

## Storage Classes

Control symbol visibility and linkage:
- **public**: Visible outside the module
- **private**: Internal to the module. Unlike `static` in C, `private` omits from the symbol table entirely.

## Calling Conventions

Specify how functions pass arguments and return values:
- **auto**: System-dependent
- **fast**: fastcall
- **std**: stdcall
- **C**: cdecl

## Attributes

### Function Attributes
Metadata attached to functions to guide optimization and code generation (e.g., `inline`, `noreturn`).

### Global Attributes
Metadata attached to global variables (e.g., `threadlocal`).
