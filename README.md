To use this piece of code:

- Go to [FLTK's website](http://fltk.org), go to Downloads and find the SVN link. Create a svn checkout right here:
	* `svn co <link> fltk`
- Now, do this:
	* `cd ./fltk && ./configure --prefix="$(pwd)" && make -j8`
- Now download latest CEF distribution and put it into this source tree as "cef". It should end up as: ./cef
	* Note, on OS X, the best-working version is: `cef_binary_3.1547.1412_macosx64`
- Make sure that you have node-gyp installed. If not, then install it:
	* `sudo npm -g install node-gyp`
	* You'll need things such as compilers, linkers and the like! And python!
- Now run: `node-gyp rebuild`.

This should build properly on OS X, if you followed above instructions. If you get a horrible flicker while running the brwoser, that is probably because FLTK does not include all the changes that I have here.
If that is the case, let me know, so I include a link to my distro.
