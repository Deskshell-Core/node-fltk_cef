// simple_app.cpp
#include "simple_app.h"
#include "simple_handler.h"
#include "include/cef_browser.h"
#include "include/cef_command_line.h"

#include <FL/x.H>
#include <string>

#ifdef __APPLE__
#include "mac.h"
#endif

SimpleApp::SimpleApp(Fl_CEF_Window *win) { this->window=win; }

void SimpleApp::OnContextInitialized() {
  REQUIRE_UI_THREAD();

  // Information used when creating the native window.
  CefWindowInfo window_info;
  #ifdef __APPLE__
  mac_set_as_child(&window_info, this->window);
  #endif


#if defined(OS_WIN)
  // On Windows we need to specify certain flags that will be passed to
  // CreateWindowEx().
  window_info.SetAsPopup(NULL, "cefsimple");
#endif

  // SimpleHandler implements browser-level callbacks.
  CefRefPtr<SimpleHandler> handler(new SimpleHandler(this->window));

  // Specify CEF browser settings here.
  CefBrowserSettings browser_settings;

  std::string url;

  // Check if a "--url=" value was provided via the command-line. If so, use
  // that instead of the default URL.
  CefRefPtr<CefCommandLine> command_line =
      CefCommandLine::GetGlobalCommandLine();
  url = command_line->GetSwitchValue("url");
  if (url.empty())
    url = "http://www.google.com";

  // Create the first browser window.
  CefBrowserHost::CreateBrowser(window_info, handler.get(), url, browser_settings);
}
