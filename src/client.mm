// native includes
#include <iostream>
using namespace std;

// FLTK
#include <FL/Fl.H>
#include <FL/Fl_Window.H>
#include <Fl/Fl_Text_Display.H>
#include <FL/Fl_Menu_Bar.H>
#include <FL/Fl_Sys_Menu_Bar.H>
#include <FL/Fl_Box.H>

#undef OVERRIDE

// Addition
#include "Fl_CEF_Window.h"

#undef OVERRIDE

// CEF
#include "include/cef_app.h"
#include "include/cef_base.h"
#include "include/cef_browser.h"
#include "include/cef_client.h"
#include "include/cef_command_line.h"
#include "include/cef_frame.h"
#include "include/cef_runnable.h"

// Fixups
#ifdef __APPLE__
#include "include/cef_application_mac.h"
#include "mac.h"
#endif

// other includes
#include "simple_app.h"
#include "simple_handler.h"

#undef OVERRIDE

// The many undefs are due to CEF and FLTK conflicting against each other with this keyword. x.x

// entry
int runCEF(int argc, char **argv) {
	// this is simply a test.
	runV8_test(argc, argv);
	
  	// Provide CEF with command-line arguments.
  	CefMainArgs main_args(argc, argv);
  	
	// Start off with an FLTK window, we need one.
	Fl_CEF_Window *win = new Fl_CEF_Window(500,500);
	#ifdef __APPLE__
  	fltk_mac_cef_ini();
  	fl_open_display();
	#endif

  	// SimpleApp implements application-level callbacks. It will create the first
  	// browser instance in OnContextInitialized() after CEF has initialized.
  	CefRefPtr<SimpleApp> app(new SimpleApp(win));

  	// Specify CEF global settings here.
  	CefSettings settings;

  	// Initialize CEF for the browser process.
  	CefInitialize(main_args, settings, app.get());

  	// Run the CEF message loop. This will block until CefQuitMessageLoop() is
  	// called.
   	win->show();   	    
  	CefRunMessageLoop();
  	
  	// Shut down CEF.
  	CefShutdown();

    return 0;
}
