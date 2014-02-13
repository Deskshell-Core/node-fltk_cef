#include <node.h>

// Externalize this for now.
extern int runCEF(int argc, char* argv[]);

using namespace v8;

Handle<Value> NJS_runCEF(const Arguments& args);
Handle<Value> NJS_runCEF(const Arguments& args) {
	HandleScope scope;
	char *argv[] = {(char*)"CEF", (char*)"--url=http://google.com", NULL};
	runCEF(2, argv);
	return scope.Close(True());
}

void InitAll(Handle<Object> exports) {
  	exports->Set(
  		String::NewSymbol("runCEF"),
      	FunctionTemplate::New(NJS_runCEF)->GetFunction()
    );
}

#ifdef GO_NATIVE
NODE_MODULE(node_fltk_cef, InitAll)
#else
NODE_MODULE(fltk_cef, InitAll)
#endif
