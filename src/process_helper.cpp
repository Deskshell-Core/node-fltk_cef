// process_helper_mac.cpp
#include <limits.h>
#include "include/cef_app.h"
#include <iostream>

// Entry point function for sub-processes.
int main(int argc, char* argv[]) {
	std::cout << "--> Helper started..." << std::endl;

  // Provide CEF with command-line arguments.
  CefMainArgs main_args(argc, argv);

  // Execute the sub-process.
  return CefExecuteProcess(main_args, NULL);
}
