#ifndef HAVE_FLTK_CEF_H
#define HAVE_FLTK_CEF_H
#include <FL/Fl_Window.h>

// generic extending.
class Fl_CEF_Window : public Fl_Window {
	public:
		Fl_CEF_Window(int height, int width);
		virtual ~Fl_CEF_Window();
		void applicationShouldTerminate();
};

#endif
