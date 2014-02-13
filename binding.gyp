{
	"variables": {
		"build_type": "Debug"
	},
	"targets": [
    	{
      		"target_name": "fltk_cef.node",
      		'dependencies': [
      			# Make sure the wrapper is included.
          		'libcef_dll_wrapper', 'CEF', 'helper'
        	],
    		"mac_bundle": 1,
    		"product_name": "fltk_cef",
      		'xcode_settings': {
        		'OTHER_CFLAGS': [
          			'-std=c++11',
   				],
      		},
      		"include_dirs": [ 
      			"fltk", 
      			"cef", "cef/include/", #So we can pull in the v8/v8.h includes. 
      			"src", "src/fltk_addons"
      		],
   			"libraries": [
   				# FLTK is static, and has some additions. Link only the most needed one.
   				"-lfltk", #Static
   				"-lpthread", 
   				"-lstdc++",
   				"-lcef"
   			],
      		"link_settings": {
      			"library_dirs": [
      				# Use .. to be more direct. GYP is so weird...
      				"../fltk/lib",
      				"../cef/<(build_type)",
      			],
      			"xcode_settings": {
      				"OTHER_LDFLAGS": [
      					"-Wl,-install_name,@loader_path/../Frameworks/Chromium\ Embedded\ Framework.framework/Libraries/libcef.dylib"
      				]
      			}
      		},
			'conditions': [
  				[ 'OS=="mac"', {
    				'link_settings': {
      					'libraries': ['-lobjc'],
    				},
    				"include_dirs": [ "src/os/mac" ],
    				"sources": [ 
    					"src/os/mac/mac.mm",
    					"src/client.mm"
    				]
  				}],
			],
			"sources": [			
				# App and Handler
				"src/node_fltk_cef.cpp",
				"src/simple_app.cpp",
				"src/simple_handler.cpp",
				"src/fltk_addons/Fl_CEF_Window.cpp",
			],
			"copies": [
				{
					"destination": "build/Release/fltk_cef.node/Contents/Frameworks",
					"files": [
						"build/Release/CEF.framework",
						"cef/<(build_type)/libplugin_carbon_interpose.dylib"
					]
				},{
					"destination": "build/Release/fltk_cef.node/Contents/Frameworks/",
					"files": [
						"build/Release/node Helper.app",
					]
				}
			],
    	},{
    		"target_name": "helper",
    		"product_name": "node Helper",
    		"type": "executable",
    		"mac_bundle": 1,
    		"product_extension": "app",
      		'dependencies': [
          		'libcef_dll_wrapper'
        	],
    		"sources": [
    			"src/process_helper.cpp"
    		],
      		'xcode_settings': {
        		'OTHER_CFLAGS': [
          			'-std=c++11',
   				],
      		},
      		"include_dirs": [ 
      			"fltk", 
      			"cef", "cef/include/", #So we can pull in the v8/v8.h includes. 
      			"src", "src/fltk_addons"
      		],
   			"libraries": [
   				# FLTK is static, and has some additions. Link only the most needed one.
   				"-lfltk", #Static
   				"-lpthread", 
   				"-lstdc++",
   				"-lcef"
   			],
      		"link_settings": {
      			"library_dirs": [
      				"../cef/<(build_type)",
      			],
      			"xcode_settings": {
      				"OTHER_LDFLAGS": [
      					"-Wl,-install_name,@executable_path/../../../../Frameworks/Chromium\ Embedded\ Framework.framework/Libraries/libcef.dylib"
      				]
      			}
      		},
    	},{
    		"target_name": "libcef_dll_wrapper",
    		"type": "static_library",
      		'xcode_settings': {
        		'OTHER_CFLAGS': [
          			'-std=c++11'
        		],
      		},
      		"include_dirs": [ 
      			"cef",
      			"cef/libcef_dll",
      			"cef/libcef_dll/wrapper",
      			"cef/libcef_dll/ctocpp",
      			"cef/libcef_dll/cpptoc",
      		],
      		"defines": [
      			"USING_CEF_SHARED"
      		],
			"sources": [
                "cef/libcef_dll//cpptoc/app_cpptoc.cc",
                "cef/libcef_dll//cpptoc/browser_process_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/client_cpptoc.cc",
                "cef/libcef_dll//cpptoc/completion_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/context_menu_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/cookie_visitor_cpptoc.cc",
                "cef/libcef_dll//cpptoc/dialog_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/display_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/domevent_listener_cpptoc.cc",
                "cef/libcef_dll//cpptoc/domvisitor_cpptoc.cc",
                "cef/libcef_dll//cpptoc/download_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/drag_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/focus_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/geolocation_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/get_geolocation_callback_cpptoc.cc",
                "cef/libcef_dll//cpptoc/jsdialog_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/keyboard_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/life_span_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/load_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/read_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/render_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/render_process_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/request_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/resource_bundle_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/resource_handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/run_file_dialog_callback_cpptoc.cc",
                "cef/libcef_dll//cpptoc/scheme_handler_factory_cpptoc.cc",
                "cef/libcef_dll//cpptoc/string_visitor_cpptoc.cc",
                "cef/libcef_dll//cpptoc/task_cpptoc.cc",
                "cef/libcef_dll//cpptoc/trace_client_cpptoc.cc",
                "cef/libcef_dll//cpptoc/urlrequest_client_cpptoc.cc",
                "cef/libcef_dll//cpptoc/v8accessor_cpptoc.cc",
                "cef/libcef_dll//cpptoc/v8handler_cpptoc.cc",
                "cef/libcef_dll//cpptoc/web_plugin_info_visitor_cpptoc.cc",
                "cef/libcef_dll//cpptoc/web_plugin_unstable_callback_cpptoc.cc",
                "cef/libcef_dll//cpptoc/write_handler_cpptoc.cc",
                "cef/libcef_dll//ctocpp/allow_certificate_error_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/auth_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/before_download_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/binary_value_ctocpp.cc",
                "cef/libcef_dll//ctocpp/browser_ctocpp.cc",
                "cef/libcef_dll//ctocpp/browser_host_ctocpp.cc",
                "cef/libcef_dll//ctocpp/callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/command_line_ctocpp.cc",
                "cef/libcef_dll//ctocpp/context_menu_params_ctocpp.cc",
                "cef/libcef_dll//ctocpp/cookie_manager_ctocpp.cc",
                "cef/libcef_dll//ctocpp/dictionary_value_ctocpp.cc",
                "cef/libcef_dll//ctocpp/domdocument_ctocpp.cc",
                "cef/libcef_dll//ctocpp/domevent_ctocpp.cc",
                "cef/libcef_dll//ctocpp/domnode_ctocpp.cc",
                "cef/libcef_dll//ctocpp/download_item_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/download_item_ctocpp.cc",
                "cef/libcef_dll//ctocpp/drag_data_ctocpp.cc",
                "cef/libcef_dll//ctocpp/file_dialog_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/frame_ctocpp.cc",
                "cef/libcef_dll//ctocpp/geolocation_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/jsdialog_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/list_value_ctocpp.cc",
                "cef/libcef_dll//ctocpp/menu_model_ctocpp.cc",
                "cef/libcef_dll//ctocpp/post_data_ctocpp.cc",
                "cef/libcef_dll//ctocpp/post_data_element_ctocpp.cc",
                "cef/libcef_dll//ctocpp/process_message_ctocpp.cc",
                "cef/libcef_dll//ctocpp/quota_callback_ctocpp.cc",
                "cef/libcef_dll//ctocpp/request_ctocpp.cc",
                "cef/libcef_dll//ctocpp/response_ctocpp.cc",
                "cef/libcef_dll//ctocpp/scheme_registrar_ctocpp.cc",
                "cef/libcef_dll//ctocpp/stream_reader_ctocpp.cc",
                "cef/libcef_dll//ctocpp/stream_writer_ctocpp.cc",
                "cef/libcef_dll//ctocpp/task_runner_ctocpp.cc",
                "cef/libcef_dll//ctocpp/urlrequest_ctocpp.cc",
                "cef/libcef_dll//ctocpp/v8context_ctocpp.cc",
                "cef/libcef_dll//ctocpp/v8exception_ctocpp.cc",
                "cef/libcef_dll//ctocpp/v8stack_frame_ctocpp.cc",
                "cef/libcef_dll//ctocpp/v8stack_trace_ctocpp.cc",
                "cef/libcef_dll//ctocpp/v8value_ctocpp.cc",
                "cef/libcef_dll//ctocpp/web_plugin_info_ctocpp.cc",
                "cef/libcef_dll//ctocpp/xml_reader_ctocpp.cc",
                "cef/libcef_dll//ctocpp/zip_reader_ctocpp.cc",
                "cef/libcef_dll//transfer_util.cpp",
                "cef/libcef_dll//wrapper/cef_byte_read_handler.cc",
                "cef/libcef_dll//wrapper/cef_stream_resource_handler.cc",
                "cef/libcef_dll//wrapper/cef_xml_object.cc",
                "cef/libcef_dll//wrapper/cef_zip_archive.cc",
                "cef/libcef_dll//wrapper/libcef_dll_wrapper.cc",
                "cef/libcef_dll//wrapper/libcef_dll_wrapper2.cc"
			]
    	},{
    		"target_name": "CEF",
    		"type": "none",
    		# We are doing this manually, because otherwise, it just wouldnt work as I want.
    		"copies": [
    			{ # "cef/Debug/libplugin_carbon_interpose.dylib",
    				"destination": "build/Release/CEF.framework/Libraries",
    				"files": [ 
    					"cef/<(build_type)/ffmpegsumo.so",
    					"cef/<(build_type)/libcef.dylib" 
    				]
    			},{
    				"destination": "build/Release/CEF.framework/",
    				"files": [ "cef/Resources/" ]
                }
    		]
    	}
  	]
}
