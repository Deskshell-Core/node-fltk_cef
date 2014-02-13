// simple_app.h
#include "Fl_CEF_Window.h"

#include "include/cef_app.h"
#include "util.h"


class SimpleApp : public CefApp,
                  public CefBrowserProcessHandler {
 public:
  SimpleApp(Fl_CEF_Window *win);
  
  // FLTK integration
  Fl_CEF_Window *window;

  // CefApp methods:
  virtual CefRefPtr<CefBrowserProcessHandler> GetBrowserProcessHandler()
      OVERRIDE { return this; }

  // CefBrowserProcessHandler methods:
  virtual void OnContextInitialized() OVERRIDE;

 private:
  // Include the default reference counting implementation.
  IMPLEMENT_REFCOUNTING(SimpleApp);
};
