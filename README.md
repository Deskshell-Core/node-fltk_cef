To use this piece of code:

- Download [FLTK](http://fltk.org) and place the source tree into this, and name it "fltk". It should end up as: ./fltk
- `cd ./fltk && ./configure --prefix="$(pwd)" && make -j8`
- Now download latest CEF distribution and put it into this source tree as "cef". It should end up as: ./cef
- Create a folder named ./cef/Default, copy the contents of Release into that folder and magically build the cef_dll_wrapper, put it in there too.
- Make sure that gcc and g++ are in your path.
- `ninja`

Before re-building, I suggest using `ninja clean` first. Look at build.ninja for build instructions...its very obvious.
