#include "Fl_CEF_Window.h"

// for safety
#undef OVERRIDE

#import "include/cef_app.h"
#import "include/cef_base.h"
#import "include/cef_browser.h"
#import "include/cef_client.h"
#import "include/cef_command_line.h"
#import "include/cef_frame.h"
#import "include/cef_runnable.h"

// other includes
#include "simple_app.h"
#include "simple_handler.h"

// We need to extend here, and call the previous constructor, adding to it too.
Fl_CEF_Window::Fl_CEF_Window(int height, int width) : Fl_Window(height, width) {
	// openApp
  this->box(FL_NO_BOX);
  this->end();
  this->resizable(this);
}
Fl_CEF_Window::~Fl_CEF_Window() {
	// Called when we're effectively killing the window
}
void Fl_CEF_Window::applicationShouldTerminate() {
	// Request that all browser windows close.
	if (SimpleHandler* handler = SimpleHandler::GetInstance()) {
		handler->CloseAllBrowsers(false);
	}
}
