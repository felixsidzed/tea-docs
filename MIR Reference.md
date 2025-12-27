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

LLVM: `%result = add %lhs, %rhs`, or `%result = fadd %lhs, %rhs` if lhs type is floating-point

Luau: `ADD Rresult Rlhs Rrhs`
</details>

#### `sub`
Subtracts the second operand from the first.
```
%result = sub %lhs, %rhs
```

<details>
<summary>Maps to</summary>

LLVM: `%result = sub %lhs, %rhs`, or `%result = fsub %lhs, %rhs` if lhs type is floating-point

Luau: `SUB Rresult Rlhs Rrhs`
</details>

#### `mul`
Multiplies two numeric values.
```
%result = mul %lhs, %rhs
```

<details>
<summary>Maps to</summary>

LLVM: `%result = mul %lhs, %rhs`, or `%result = fmul %lhs, %rhs` if lhs type is floating-point

Luau: `MUL Rresult Rlhs Rrhs`
</details>

#### `div`
Divides the first operand by the second. Signedness is determined by the first operand's type.
```
%result = div %lhs, %rhs
```

<details>
<summary>Maps to</summary>

LLVM: `%result = sdiv %lhs, %rhs` if lhs is signed, `%result = udiv %lhs, %rhs` if lhs type is unsigned, or `%result = fdiv %lhs, %rhs` if lhs is floating-point

Luau: `DIV Rresult Rlhs Rrhs`
</details>

#### `mod`
Computes the remainder of division.
```
%result = mod %lhs, %rhs
```

<details>
<summary>Maps to</summary>

LLVM: `%result = srem %lhs, %rhs` if lhs is signed, `%result = urem %lhs, %rhs` if lhs type is unsigned, or `%result = frem %lhs, %rhs` if lhs is floating-point

Luau: `MOD Rresult Rlhs Rrhs`
</details>

### Bitwise Operations

#### `not`
Performs bitwise negation.
```
%result = not %operand
```

<details>
<summary>Maps to</summary>

LLVM: `%result = xor %operand, -1`

Luau: `NOT Rresult Roperand`
</details>

#### `and`
Performs bitwise AND.
```
%result = and %lhs, %rhs
```

<details>
<summary>Maps to</summary>

LLVM: `%result = and %lhs, %rhs`

Luau: `AND Rresult Rlhs Rrhs`
</details>

#### `or`
Performs bitwise OR.
```
%result = or %lhs, %rhs
```

<details>
<summary>Maps to</summary>

LLVM: `%result = or %lhs, %rhs`

Luau: `OR Rresult Rlhs Rrhs`
</details>

#### `xor`
Performs bitwise exclusive OR.
```
%result = xor %lhs, %rhs
```

<details>
<summary>Maps to</summary>

LLVM: `%result = xor %lhs, %rhs`

Luau:
```
GETIMPORT Rfunc "bit32.bxor"
; load arguments into Rfunc+1, Rfunc+2
CALL Rfunc 3 2
MOVE Rresult Rfunc
```
</details>

#### `shl`
Shifts bits left.
```
%result = shl %value, %amount
```

<details>
<summary>Maps to</summary>

LLVM: `%result = shl %value, %amount`

Luau:
```
GETIMPORT Rfunc "bit32.lshift"
; load arguments into Rfunc+1, Rfunc+2
CALL Rfunc 3 2
MOVE Rresult Rfunc
```
</details>

#### `shr`
Shifts bits right.
```
%result = shr %value, %amount
```

<details>
<summary>Maps to</summary>

LLVM: `%result = ashr %value, %amount` if value is signed, or `%result = lshr %value, %amount` if unsigned

Luau:
```
GETIMPORT Rfunc "bit32.rshift"
; load arguments into Rfunc+1, Rfunc+2
CALL Rfunc 3 2
MOVE Rresult Rfunc
```
</details>

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

<details>
<summary>Maps to</summary>

LLVM: `%result = icmp <predicate> %lhs, %rhs`

Luau (varies by predicate):
- `eq`:
```
JUMPIFEQ Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `neq`:
```
JUMPIFNOTEQ Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `sgt/ugt`:
```
JUMPIFLT Rrhs Rlhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `sge/uge`:
```
JUMPIFLE Rrhs Rlhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `slt/ult`:
```
JUMPIFLT Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `sle/ule`:
```
JUMPIFLE Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
</details>

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

<details>
<summary>Maps to</summary>

LLVM: `%result = fcmp <predicate> %lhs, %rhs`

Luau:
- `oeq`:
```
JUMPIFEQ Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `oneq`:
```
JUMPIFNOTEQ Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `ogt`:
```
JUMPIFLT Rrhs Rlhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `oge`:
```
JUMPIFLE Rrhs Rlhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `olt`:
```
JUMPIFLT Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
- `ole`:
```
JUMPIFLE Rlhs Rrhs 2
LOADB Rresult 0 1
LOADB Rresult 1 0
```
</details>

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

<details>
<summary>Maps to</summary>

LLVM: `%result = load %ptr` (with optional `volatile` flag)

Luau: If ptr is a local slot, `MOVE Rresult Rptr`, otherwise:
```
GETIMPORT Rfunc "__builtin_memread"
; load ptr into Rfunc+1
CALL Rfunc 2 2
MOVE Rresult Rfunc
```
</details>

#### `store`
Writes a value to memory.
```
store %pointer, %value
```
Supports a volatile flag for preventing optimization.
```
volatile store %pointer, %value
```

<details>
<summary>Maps to</summary>

LLVM: `store %value, %pointer` (with optional `volatile` flag)

Luau: If pointer is a local slot, `MOVE Rptr Rvalue`, otherwise:
```
GETIMPORT Rfunc "__builtin_memwrite"
; load pointer into Rfunc+1
MOVE Rfunc+2 Rvalue
CALL Rfunc 3 1
```
</details>

#### `alloca`
Allocates stack memory for a value of the specified type.
```
%result = alloca type
```

<details>
<summary>Maps to</summary>

LLVM: `%result = alloca <type>`

Luau: No instruction. Reserves a register
</details>

#### `gep`
Computes the address of an element within an aggregate type (array or struct).
```
%result = gep %pointer, %index
%result = gep %pointer, %index1, %index2, ...
```

<details>
<summary>Maps to</summary>

LLVM: `%result = getelementptr %pointer, %index1, %index2, ...`

Luau: Not supported
</details>

### Control Flow

#### `br`
Unconditional branch to a basic block.
```
br %target
```

<details>
<summary>Maps to</summary>

LLVM: `br label %target`

Luau: `JUMP target`
</details>

#### `cbr`
Conditional branch based on a boolean predicate.
```
cbr %pred, %true_block, %false_block
```

<details>
<summary>Maps to</summary>

LLVM: `br i1 %pred, label %true_block, label %false_block`

Luau:
```
JUMPIF Rpred true_block
JUMP false_block
```
</details>

#### `ret`
Returns from the current function.
```
ret %value
ret void
```

<details>
<summary>Maps to</summary>

LLVM: `ret %value` or `ret void`

Luau: `RETURN Rvalue 2` or `RETURN 0 1` for void
</details>

#### `phi`
PHI node for SSA form, merging values from different predecessor blocks.
```
%result = phi [%value1, %block1], [%value2, %block2], ...
```

<details>
<summary>Maps to</summary>

LLVM: `%result = phi <type> [%value1, %block1], [%value2, %block2], ...`

Luau: Not supported
</details>

### Function Operations

#### `call`
Invokes a function with arguments.
```
%result = call %function(%arg1, %arg2, ...)
```

<details>
<summary>Maps to</summary>

LLVM: `%result = call <type> %function(%arg1, %arg2, ...)`

Luau:
```
; move arguments to consecutive registers starting at Rcallee+1
MOVE Rcallee+1 Rarg1
MOVE Rcallee+2 Rarg2
...
CALL Rcallee nargs+1 nret
MOVE Rresult Rcallee ; omitted if callee returns void
```
</details>

### Miscellaneous

#### `nop`
No operation; does nothing.
```
nop
```

<details>
<summary>Maps to</summary>

LLVM: No instruction emitted

Luau: No instruction emitted
</details>

#### `cast`
Converts a value from one type to another.
```
%result = cast %value to type
```

<details>
<summary>Maps to</summary>

LLVM:
- float to int: `fptosi` or `fptoui`
- int to float: `sitofp` or `uitofp`
- int to int: `sext`, `zext`, or `trunc`
- pointer to int: `ptrtoint`
- int to pointer: `inttoptr`
- other: `bitcast`

Luau: No instruction; Luau is dynamically typed
</details>

#### `unreachable`
Indicates that this code path should never be reached.
```
unreachable
```

<details>
<summary>Maps to</summary>

LLVM: `unreachable`

Luau: `RETURN 0 1`
</details>

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
