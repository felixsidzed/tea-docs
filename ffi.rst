FFI (Foreign Function Interface)
================================

Detailed documentation for the FFI support of the Tea programming language.

Introduction
------------

The Foreign Function Interface (FFI) in Tea provides a mechanism to call functions written in other programming languages, primarily C.
This allows Tea programs to leverage existing libraries and interfaces with system resources that may not be directly accessible through the Tea standard library.

My First FFI Module
-------------------

Let's start with a simple example to demonstrate how to create an FFI module in Tea.

.. dropdown:: Step 1: Define your C function

	First, let's create a simple C function that we want to call from Tea:

	.. code:: c

		// myModule.c
		int _myModule__add(int a, int b) {
		  return a + b;
		}

.. dropdown:: Step 2: Create the declaration in Tea

	Now, we'll create a Tea module that declares our function:

	.. code:: tea

		// myModule.tea
		import __cdecl func add(int a, int b) -> int;

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
		  var result = myModule::add(40, 2);
		  io::printf("The result is: %d\n", result); // Output: The result is: 42

		  return 0;
		end

	Don't forget to link against ``myModule.lib``!

Tea Module Format
=================

Tea uses a custom module format to declare Foreign Function Interface (FFI) functions, allowing Tea programs to interface with functions implemented in other languages.
Tea modules are defined using `import` declarations in Tea source files.

Syntax
------

.. code-block:: tea

	import __cdecl func myFunction(int argument) -> int;

Supported Types
---------------

See :ref:`tea-types`
