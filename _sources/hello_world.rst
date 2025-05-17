Hello, World!
=============

Your first program in Tea - A "Hello, World!" program

Source Code
-----------

.. code-block:: tea
	:linenos:

	// Import the I/O module from the standard library
	using "io";

	// Define the entry point for our program
	public func main() -> int
		// Print "Hello, World!" to console
		io::print("Hello, World!\n");

		return 0;
	end

Compiling
---------

.. code-block:: bash

    tea hello-world.tea -o hello-world.o

.. dropdown:: Windows

	.. note:: Make sure you have C++ Build Tools installed (for *link.exe* and *kernel32.lib*)

	.. code-block:: bash

		# Link the generated .o file with Tea's standard library and kernel32
		link /entry:main /subsystem:console /out:hello-world.exe hello-world.o teastd.lib kernel32.lib

		# Run the generated .exe
		hello-world.exe

.. dropdown:: Linux

	.. note::

		TODO
