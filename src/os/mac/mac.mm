#include <FL/x.H>
#include <FL/Fl_Window.H>
#include "Fl_CEF_Window.h"
#import <Cocoa/Cocoa.h>
#include "include/cef_browser.h"

void* prepare_FL_Window_for_cef(Fl_CEF_Window* win) {
 NSView *current_focus = [NSView focusView]; 
 [current_focus unlockFocus];
 [[fl_xid(win) contentView]  lockFocus];
 return (void*)current_focus;
}

void release_after_cef(void *view) {
 NSView *current_focus = [NSView focusView]; 
 [current_focus unlockFocus];
 [(NSView*)view lockFocus];
}

void mac_set_as_child(CefWindowInfo *winin, Fl_CEF_Window *win) {
	winin->SetAsChild(
		[fl_xid(win) contentView],
		0, 0, 500, 500
	);
}

void fltk_mac_cef_ini()
{
  [NSApplication sharedApplication];
  [NSApp setServicesMenu:[[NSMenu alloc] initWithTitle:@""]];
}
