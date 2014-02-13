#include <FL/x.H>
#include <FL/Fl_Window.H>
#include "Fl_CEF_Window.h"
#include "include/cef_browser.h"

void* prepare_FL_Window_for_cef(Fl_CEF_Window* win);
void release_after_cef(void *view);
void mac_set_as_child(CefWindowInfo *winin, Fl_CEF_Window *win);
void fltk_mac_cef_ini();
