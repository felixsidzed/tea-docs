FFI (Foreign Function Interface)
================================

Detailed documentation for the FFI support of the Tea programming language.

.. warning::
	
	This page is not verified and requires editing

Introduction
------------

The Foreign Function Interface (FFI) in Tea provides a mechanism to call functions written in other programming languages, primarily C. This allows Tea programs to leverage existing libraries and interfaces with system resources that may not be directly accessible through the Tea standard library.

My First FFI Module
-------------------

Let's start with a simple example to demonstrate how to create an FFI module in Tea.

.. dropdown:: Step 1: Define your C function

	First, let's create a simple C function that we want to call from Tea:

	.. code:: c

		// myModule.c
		// namespacing with "_(module name)__(function name)" is optional, but recommended to avoid naming issues
		int _myModule__add(int a, int b) {
		  return a + b;
		}

.. dropdown:: Step 2: Create the Tea FFI binding

	Now, we'll create a Tea module that declares our function:

	.. code:: c

		// myModule.json
		{
		  "format": 3,
		  "namespace": "_myModule__", // This depends on how you defined your function.
		                              // Internally, Tea will concatenate this with the function being called.
		                              // For example: _myModule__myFunction
		                              // If you do not have a namespace (for example defined as: myFunction), leave this empty
		  "functions": {
		    // Declare our function
		    "add": {
		      "return": "INT",
		      "args": ["INT", "INT"],
		      "vararg": false
		    }
		  }
		}

.. dropdown:: Step 3: Building and using the module

	Compile the C code into a shared library:

	.. code:: bash

		$ clang -c myModule.c -o myModule.o
		$ ar rcs myModule.lib myModule.o

.. dropdown:: Step 4: Now, you can use the module in your Tea code

	.. code:: tea

		using "io";
		using "myModule";

		public func main() -> int
			var result: int = myModule::add(40, 2);
			io::printf("The result is: %d\n", result); // Output: The result is: 42

			return 0;
		end

Tea Module Format
=================

Tea uses a custom module format to declare Foreign Function Interface (FFI) functions, allowing Tea programs to interface with functions implemented in other languages.
A Tea module is defined in a JSON file with the following key fields:

.. dropdown:: ``format``

   **Required**

   Specifies the version of the Tea module format.

   - Currently, the only valid value is ``3``.
   - This field is used to ensure compatibility with the Tea compiler.

.. dropdown:: ``namespace``

   **Required**

   Defines the namespace prefix that will be prepended to function names.

   - The namespace is concatenated with the function name when Tea calls the function internally.
   - Example: If ``namespace`` is ``"_myModule__"`` and the function is ``"add"``, Tea will call ``"_myModule__add"``.
   - If your functions don't use a namespace in their implementation, use an empty string ``""``.

.. dropdown:: ``functions``

   **Required**

   An object containing function declarations, where each key is the function name and the value is an object describing the function signature.

   Each function definition includes:
   
   - ``return``: The return type of the function.
   - ``args``: An array of parameter types the function accepts.
   - ``vararg``: A boolean indicating whether the function accepts a variadic number of arguments.

.. dropdown:: Supported Types

   Tea modules support the following data types for function arguments and return values:

   - **INT**: 32-bit integer
   - **FLOAT**: Single precision floating-point
   - **DOUBLE**: Double precision floating-point
   - **CHAR**: Single character (8-bit integer)
   - **STRING**: Text string
   - **VOID**: No return value
   - **BOOL**: Boolean (true/false)
   - **LONG**: 64-bit integer

.. dropdown:: Usage Notes

   - The module file should be named with a ``.json`` extension.
   - The ``namespace`` should match how your function is implemented in native code.
   - Functions must be explicitly declared before they can be called from Tea.
   - The ``vararg`` property allows functions to accept a variable number of arguments after the specified ones.
