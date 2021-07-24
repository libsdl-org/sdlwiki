Last login: Wed Jul 21 21:51:11 on console
tdh@iMac-van-Tjarko ~ % 
  [Restored 24 Jul 2021 at 16:31:26]
Last login: Sat Jul 24 16:26:27 on console
Restored session: Thu Jul 22 00:21:53 CEST 2021
tdh@i7mac40 ~ % mkdir functions
tdh@i7mac40 ~ % cd functions
tdh@i7mac40 functions % mkdir py
tdh@i7mac40 functions % mkdir php
tdh@i7mac40 functions % mkdir java
tdh@i7mac40 functions % cd ..
tdh@i7mac40 ~ % cd /Volumes 
tdh@i7mac40 /Volumes % cd Data-3TB 
tdh@i7mac40 Data-3TB % cd Users 
tdh@i7mac40 Users % cd Sources 
tdh@i7mac40 Sources % cd gsplus
tdh@i7mac40 gsplus % cd build
tdh@i7mac40 build % rm -R *
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:35:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_mouse.h:32:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:111:14: error: expected ';' after top level declarator
} SDL_SetHint
             ^
             ;
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:112:12: error: redefinition of 'SDL_bool' as different kind of symbol
extern int SDL_bool;
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_stdinc.h:96:3: note: previous definition is here
} SDL_bool;
  ^
2 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % rm -R *
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:35:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_mouse.h:32:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:115:24: error: expected ';' at end of declaration list
        Uint8 SDL_FALSE 0;
                       ^
                       ;
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:116:23: error: expected ';' at end of declaration list
        Uint8 SDL_TRUE 1;
                      ^
                      ;
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:117:3: error: typedef redefinition with different types ('struct SDL_bool' vs 'enum SDL_bool')
} SDL_bool;
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_stdinc.h:96:3: note: previous definition is here
} SDL_bool;
  ^
3 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % cmake ..               
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % rm -R *
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  6%] Linking C static library libx_readline.a
[  6%] Built target x_readline
[  8%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  9%] Linking C executable vmnet_helper
[  9%] Built target vmnet_helper
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:35:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_mouse.h:32:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:117:3: error: typedef redefinition with different types ('struct SDL_bool' vs 'enum SDL_bool')
} SDL_bool;
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_stdinc.h:96:3: note: previous definition is here
} SDL_bool;
  ^
1 error generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % rm -R *                
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..               
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:35:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_mouse.h:32:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:114:2: error: invalid preprocessing directive
#typedef struct SDL_bool {
 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:115:10: error: invalid preprocessing directive
#        Uint8 SDL_FALSE;
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:116:10: error: invalid preprocessing directive
#        Uint8 SDL_TRUE;
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:117:2: error: invalid preprocessing directive
#} SDL_bool;
 ^
4 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % rm -R *                
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..               
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make                   
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  6%] Linking C static library libx_readline.a
[  6%] Built target x_readline
[  8%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  9%] Linking C executable vmnet_helper
[  9%] Built target vmnet_helper
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:5: error: use of undeclared identifier 'SDLK_KP_NUMLOCKCLEAR'
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:349:12: error: implicit declaration of function 'SDL_CreateWindow' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  window = SDL_CreateWindow(
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:349:12: note: did you mean 'SDL_CreateCond'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_mutex.h:138:36: note: 'SDL_CreateCond' declared here
extern DECLSPEC SDL_cond * SDLCALL SDL_CreateCond(void);
                                   ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:349:10: warning: incompatible integer to pointer conversion assigning to 'SDL_Window *' (aka 'struct SDL_Window *') from 'int' [-Wint-conversion]
  window = SDL_CreateWindow(
         ^ ~~~~~~~~~~~~~~~~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:379:14: error: implicit declaration of function 'SDL_CreateRenderer' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  renderer = SDL_CreateRenderer(window, -1, renderer_hints);
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:379:12: warning: incompatible integer to pointer conversion assigning to 'SDL_Renderer *' (aka 'struct SDL_Renderer *') from 'int' [-Wint-conversion]
  renderer = SDL_CreateRenderer(window, -1, renderer_hints);
           ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
217 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % rm -R *                
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:5: error: use of undeclared identifier 'SDLK_KP_NUMLOCKCLEAR'
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:379:14: error: implicit declaration of function 'SDL_CreateRenderer' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  renderer = SDL_CreateRenderer(window, -1, renderer_hints);
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:379:12: warning: incompatible integer to pointer conversion assigning to 'SDL_Renderer *' (aka 'struct SDL_Renderer *') from 'int' [-Wint-conversion]
  renderer = SDL_CreateRenderer(window, -1, renderer_hints);
           ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:388:13: error: implicit declaration of function 'SDL_CreateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  texture = SDL_CreateTexture(renderer,
            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:388:13: note: did you mean 'SDL_CreateRenderer'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:379:14: note: 'SDL_CreateRenderer' declared here
  renderer = SDL_CreateRenderer(window, -1, renderer_hints);
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:388:11: warning: incompatible integer to pointer conversion assigning to 'SDL_Texture *' (aka 'struct SDL_Texture *') from 'int' [-Wint-conversion]
  texture = SDL_CreateTexture(renderer,
          ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:394:19: warning: incompatible integer to pointer conversion assigning to 'SDL_Texture *' (aka 'struct SDL_Texture *') from 'int' [-Wint-conversion]
  overlay_texture = SDL_CreateTexture(renderer,
                  ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
fatal error: too many errors emitted, stopping now [-ferror-limit=]
218 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % rm -R * 
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % cmake ..
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  6%] Linking C static library libx_readline.a
[  6%] Built target x_readline
[  8%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  9%] Linking C executable vmnet_helper
[  9%] Built target vmnet_helper
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:5: error: use of undeclared identifier 'SDLK_KP_NUMLOCKCLEAR'
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:388:13: error: implicit declaration of function 'SDL_CreateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  texture = SDL_CreateTexture(renderer,
            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:388:13: note: did you mean 'SDL_CreateRenderer'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:134:16: note: 'SDL_CreateRenderer' declared here
SDL_Renderer * SDL_CreateRenderer(SDL_Window * window,
               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:388:11: warning: incompatible integer to pointer conversion assigning to 'SDL_Texture *' (aka 'struct SDL_Texture *') from 'int' [-Wint-conversion]
  texture = SDL_CreateTexture(renderer,
          ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:394:19: warning: incompatible integer to pointer conversion assigning to 'SDL_Texture *' (aka 'struct SDL_Texture *') from 'int' [-Wint-conversion]
  overlay_texture = SDL_CreateTexture(renderer,
                  ^ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:400:3: error: implicit declaration of function 'SDL_SetTextureBlendMode' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_SetTextureBlendMode(overlay_texture, SDL_BLENDMODE_BLEND);
  ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
217 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_video.h
tdh@i7mac40 build % rm -R *
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..               
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
tdh@i7mac40 build % make                   
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  6%] Linking C static library libx_readline.a
[  6%] Built target x_readline
[  8%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  9%] Linking C executable vmnet_helper
[  9%] Built target vmnet_helper
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:5: error: use of undeclared identifier 'SDLK_KP_NUMLOCKCLEAR'
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 1
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:400:3: error: implicit declaration of function 'SDL_SetTextureBlendMode' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_SetTextureBlendMode(overlay_texture, SDL_BLENDMODE_BLEND);
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(overlay_texture, &dstrect, overlay_pixels, pitch*sizeof(Uint32) );
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: note: did you mean 'SDL_CreateTexture'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:129:15: note: 'SDL_CreateTexture' declared here
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
              ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
215 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/sdl2_driver.c
tdh@i7mac40 build % rm -R *
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..;make
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  6%] Linking C static library libx_readline.a
[  6%] Built target x_readline
[  8%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  9%] Linking C executable vmnet_helper
[  9%] Built target vmnet_helper
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:5: error: use of undeclared identifier 'SDLK_KP_NUMLOCKCLEAR'
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 'linear'
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 'linear'
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:400:3: error: implicit declaration of function 'SDL_SetTextureBlendMode' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_SetTextureBlendMode(overlay_texture, SDL_BLENDMODE_BLEND);
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(overlay_texture, &dstrect, overlay_pixels, pitch*sizeof(Uint32) );
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: note: did you mean 'SDL_CreateTexture'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:129:15: note: 'SDL_CreateTexture' declared here
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
              ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
215 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/sdl2_keyboard.h
tdh@i7mac40 build % cd ..
tdh@i7mac40 gsplus % cd src
tdh@i7mac40 src % ls -als
total 6992
   0 drwxr-xr-x  150 tdh  admin    4800 Jul 24 22:18 .
   0 drwxr-xr-x   24 tdh  admin     768 Jul  7 17:30 ..
  48 -rw-r--r--@   1 tdh  admin   18436 Jul 12 11:55 .DS_Store
  32 -rw-r--r--    1 tdh  admin    8247 Jul  7 17:16 CMakeLists.txt
  16 -rw-r--r--    1 tdh  admin     245 Jul  7 17:16 GSplus.bat
  32 -rw-r--r--    1 tdh  admin   11214 Jul  7 17:16 INTERNALS.iwm
  16 -rw-r--r--    1 tdh  admin    4192 Jul  7 17:16 INTERNALS.overview
  16 -rw-r--r--    1 tdh  admin    7563 Jul  7 17:16 INTERNALS.xdriver
  16 -rw-r--r--    1 tdh  admin     249 Jul  7 17:16 Makefile
  16 -rw-r--r--    1 tdh  admin    3282 Jul 11 23:22 SDL.h
  16 -rw-r--r--    1 tdh  admin    1934 Jul  7 17:47 SDL_active.h
  32 -rw-r--r--    1 tdh  admin   11216 Jul  7 17:41 SDL_audio.h
  16 -rw-r--r--    1 tdh  admin    6049 Jul  7 17:44 SDL_cdrom.h
  16 -rw-r--r--    1 tdh  admin    1475 Jul  7 17:39 SDL_config.h
  16 -rw-r--r--    1 tdh  admin    4194 Jul  7 17:40 SDL_config_macosx.h
  16 -rw-r--r--    1 tdh  admin    2222 Jul  7 17:45 SDL_cpuinfo.h
  16 -rw-r--r--    1 tdh  admin    6056 Jul  7 17:43 SDL_endian.h
  16 -rw-r--r--    1 tdh  admin    1875 Jul  7 17:42 SDL_error.h
  32 -rw-r--r--    1 tdh  admin   13042 Jul  7 17:46 SDL_events.h
  16 -rw-r--r--    1 tdh  admin    5533 Jul  7 17:50 SDL_joystick.h
  16 -rw-r--r--    1 tdh  admin    4099 Jul  7 17:48 SDL_keyboard.h
  32 -rw-r--r--@   1 tdh  admin    9249 Jul 12 12:05 SDL_keysym.h
  16 -rw-r--r--    1 tdh  admin    2740 Jul  7 17:53 SDL_loadso.h
  16 -rw-r--r--    1 tdh  admin    2867 Jul  7 17:35 SDL_main.h
  16 -rw-r--r--    1 tdh  admin    4755 Jul  7 17:49 SDL_mouse.h
  16 -rw-r--r--    1 tdh  admin    5861 Jul  7 17:43 SDL_mutex.h
  16 -rw-r--r--    1 tdh  admin    2710 Jul  7 17:39 SDL_platform.h
  16 -rw-r--r--    1 tdh  admin    2010 Jul  7 17:50 SDL_quit.h
  16 -rw-r--r--    1 tdh  admin    4959 Jul  7 17:44 SDL_rwops.h
  48 -rw-r--r--    1 tdh  admin   16474 Jul  7 17:38 SDL_stdinc.h
  16 -rw-r--r--    1 tdh  admin    5861 Jul  7 17:44 SDL_thread.h
  16 -rw-r--r--    1 tdh  admin    4528 Jul  7 17:54 SDL_timer.h
  16 -rw-r--r--    1 tdh  admin    2638 Jul  7 17:54 SDL_version.h
 160 -rw-r--r--    1 tdh  admin   79277 Jul  7 18:25 SDL_video.c
  80 -rw-r--r--    1 tdh  admin   39131 Jul 24 22:14 SDL_video.h
  96 -rw-r--r--    1 tdh  admin   48968 Jul  7 17:16 adb.c
  16 -rw-r--r--    1 tdh  admin    4825 Jul  7 17:16 adb.h
  16 -rw-r--r--    1 tdh  admin    6510 Jul  7 17:16 adb_keycodes.h
   0 drwxr-xr-x    5 tdh  admin     160 Jul 11 23:41 arch
   0 drwxr-xr-x   10 tdh  admin     320 Jul  7 17:16 assets
   0 drwxr-xr-x   17 tdh  admin     544 Jul  7 17:16 atbridge
  16 -rw-r--r--    1 tdh  admin    5231 Jul  7 17:41 begin_code.h
  32 -rw-r--r--    1 tdh  admin   10937 Jul  7 17:16 clock.c
  16 -rw-r--r--    1 tdh  admin    1483 Jul  7 17:41 close_code.h
  16 -rw-r--r--    1 tdh  admin     261 Jul  7 17:16 compile_time.c
 192 -rw-r--r--    1 tdh  admin   97446 Jul  7 17:16 config.c
  16 -rw-r--r--    1 tdh  admin    2162 Jul  7 17:16 config.h
  16 -rw-r--r--    1 tdh  admin    2009 Jul  7 17:16 config.txt
  96 -rw-r--r--    1 tdh  admin   41988 Jul  7 17:16 debug.c
  16 -rw-r--r--    1 tdh  admin     191 Jul  7 17:16 debug.h
  48 -rw-r--r--    1 tdh  admin   22587 Jul  7 17:16 debug_miniasm.re2c
  80 -rw-r--r--    1 tdh  admin   37899 Jul  7 17:16 debug_shell.re2c
  32 -rw-r--r--    1 tdh  admin    8677 Jul  7 17:16 debug_sweet16.re2c
  32 -rw-r--r--    1 tdh  admin   12681 Jul  7 17:16 debug_template.re2c
  32 -rw-r--r--    1 tdh  admin    8568 Jul  7 17:16 defc.h
  16 -rw-r--r--    1 tdh  admin    5246 Jul  7 17:16 defcomm.h
  16 -rw-r--r--    1 tdh  admin     940 Jul  7 17:16 defs.h
  80 -rw-r--r--    1 tdh  admin   34138 Jul  7 17:16 defs_instr.h
  16 -rw-r--r--    1 tdh  admin     227 Jul  7 17:16 disasm.c
  16 -rw-r--r--    1 tdh  admin     499 Jul  7 17:16 disasm.h
  80 -rw-r--r--    1 tdh  admin   36643 Jul  7 17:16 engine_c.c
 112 -rw-r--r--    1 tdh  admin   51253 Jul  7 17:16 engine_s.s
  32 -rw-r--r--    1 tdh  admin   13698 Jul  7 17:16 fbdriver.c
  16 -rw-r--r--    1 tdh  admin     507 Jul  7 17:16 fix_mac_menu.m
  16 -rw-r--r--    1 tdh  admin    4884 Jul  7 17:16 fst.h
  16 -rw-r--r--    1 tdh  admin    1189 Jul  7 17:16 glog.c
  16 -rw-r--r--    1 tdh  admin     171 Jul  7 17:16 glog.h
  32 -rw-r--r--    1 tdh  admin    8397 Jul  7 17:16 gsos.h
  96 -rw-r--r--    1 tdh  admin   42280 Jul  7 17:16 gsport32.aps
  16 -rw-r--r--    1 tdh  admin    7279 Jul  7 17:16 gsport32.rc
  48 -rw-r--r--    1 tdh  admin   20931 Jul  7 17:16 gsportfont.h
  16 -rw-r--r--    1 tdh  admin    4334 Jul  7 17:16 headless_driver.c
  32 -rw-r--r--    1 tdh  admin   10551 Jul  7 17:16 host_common.c
  16 -rw-r--r--    1 tdh  admin    3945 Jul  7 17:16 host_common.h
  96 -rw-r--r--    1 tdh  admin   44154 Jul  7 17:16 host_fst.c
  80 -rw-r--r--    1 tdh  admin   35246 Jul  7 17:16 host_mli.c
1680 -rw-r--r--    1 tdh  admin  854528 Jul  7 17:16 icongs.h
 128 -rw-r--r--    1 tdh  admin   60632 Jul  7 17:16 imagewriter.cpp
  32 -rw-r--r--    1 tdh  admin   10377 Jul  7 17:16 imagewriter.h
  96 -rw-r--r--    1 tdh  admin   44298 Jul  7 17:16 instable.h
  16 -rw-r--r--    1 tdh  admin    3430 Jul  7 17:16 iw_charmaps.h
 112 -rw-r--r--    1 tdh  admin   56457 Jul  7 17:16 iwm.c
  16 -rw-r--r--    1 tdh  admin    1873 Jul  7 17:16 iwm.h
  16 -rw-r--r--    1 tdh  admin    7412 Jul  7 17:16 iwm_35_525.h
  32 -rw-r--r--    1 tdh  admin    9415 Jul  7 17:16 joystick_driver.c
  48 -rw-r--r--    1 tdh  admin   21091 Jul  7 17:16 macdriver_console.c
  32 -rw-r--r--    1 tdh  admin   12111 Jul  7 17:16 macdriver_generic.c
  16 -rw-r--r--    1 tdh  admin    3721 Jul  7 17:16 macsnd_driver.c
  16 -rw-r--r--    1 tdh  admin     560 Jul  7 17:16 make_inst
  16 -rw-r--r--    1 tdh  admin     608 Jul  7 17:16 make_size
  16 -rw-r--r--    1 tdh  admin      49 Jul  7 17:16 make_win
  16 -rw-r--r--    1 tdh  admin    1564 Jul  7 17:16 mnemonics.x
 160 -rw-r--r--    1 tdh  admin   75057 Jul  7 17:16 moremem.c
  32 -rw-r--r--    1 tdh  admin    9602 Jul  7 17:16 op_routs.h
  16 -rw-r--r--    1 tdh  admin    7680 Jul  7 17:16 opcodes.x
  48 -rw-r--r--    1 tdh  admin   18707 Jul  7 17:16 options.c
  16 -rw-r--r--    1 tdh  admin     116 Jul  7 17:16 options.h
  16 -rw-r--r--    1 tdh  admin    4673 Jul  7 17:16 paddles.c
  16 -rw-r--r--    1 tdh  admin    1766 Jul  7 17:16 parallel.c
  16 -rw-r--r--    1 tdh  admin     256 Jul  7 17:16 parallel.rom
  16 -rw-r--r--    1 tdh  admin    3406 Jul  7 17:16 partls.c
 112 -rw-r--r--    1 tdh  admin   55746 Jul  7 17:16 printer.cpp
  32 -rw-r--r--    1 tdh  admin    9778 Jul  7 17:16 printer.h
  64 -rw-r--r--    1 tdh  admin   28122 Jul  7 17:16 printer_charmaps.h
  16 -rw-r--r--    1 tdh  admin    1731 Jul  7 17:16 prodos.h
  16 -rw-r--r--    1 tdh  admin    1709 Jul  7 17:16 prodos_protos.h
  48 -rw-r--r--    1 tdh  admin   20351 Jul  7 17:16 protos.h
  16 -rw-r--r--    1 tdh  admin    1680 Jul  7 17:16 protos_engine_c.h
  16 -rw-r--r--    1 tdh  admin    1133 Jul  7 17:16 protos_macdriver.h
  16 -rw-r--r--    1 tdh  admin     418 Jul  7 17:16 protos_macsnd_driver.h
  16 -rw-r--r--    1 tdh  admin    1338 Jul  7 17:16 protos_windriver.h
  16 -rw-r--r--    1 tdh  admin    1612 Jul  7 17:16 protos_xdriver.h
   0 drwxr-xr-x   18 tdh  admin     576 Jul  7 17:16 rawnet
  16 -rw-r--r--    1 tdh  admin    5210 Jul  7 17:16 readline.c
  16 -rw-r--r--    1 tdh  admin    2348 Jul  7 17:16 resource
  16 -rw-r--r--    1 tdh  admin    2215 Jul  7 17:16 resource.h
  96 -rw-r--r--    1 tdh  admin   43471 Jul  7 17:16 scc.c
  16 -rw-r--r--    1 tdh  admin    2094 Jul  7 17:16 scc.h
  16 -rw-r--r--    1 tdh  admin    4055 Jul  7 17:16 scc_imagewriter.c
  16 -rw-r--r--    1 tdh  admin    3551 Jul  7 17:16 scc_llap.c
  16 -rw-r--r--    1 tdh  admin     423 Jul  7 17:16 scc_llap.h
  16 -rw-r--r--    1 tdh  admin    4438 Jul  7 17:16 scc_macdriver.c
  64 -rw-r--r--    1 tdh  admin   31117 Jul  7 17:16 scc_socket_driver.c
  16 -rw-r--r--    1 tdh  admin    5955 Jul  7 17:16 scc_windriver.c
  64 -rw-r--r--@   1 tdh  admin   27805 Jul 24 22:16 sdl2_driver.c
  16 -rw-r--r--    1 tdh  admin       2 Jul 24 22:18 sdl2_keyboard.h
  16 -rw-r--r--    1 tdh  admin    5390 Jul  7 17:16 sdl2snd_driver.c
  16 -rw-r--r--    1 tdh  admin    4881 Jul  7 17:16 sdlsnd_driver.c
 128 -rw-r--r--    1 tdh  admin   62471 Jul  7 17:16 sim65816.c
  32 -rw-r--r--    1 tdh  admin    9107 Jul  7 17:16 size_tab.h
  48 -rw-r--r--    1 tdh  admin   21061 Jul  7 17:16 smartport.c
 112 -rw-r--r--    1 tdh  admin   50082 Jul  7 17:16 sound.c
  16 -rw-r--r--    1 tdh  admin    1260 Jul  7 17:16 sound.h
  32 -rw-r--r--    1 tdh  admin    9223 Jul  7 17:16 sound_driver.c
  16 -rw-r--r--    1 tdh  admin    4566 Jul  7 17:16 superhires.h
  16 -rw-r--r--    1 tdh  admin    1729 Jul  7 17:16 support.h
   0 drwxr-xr-x    9 tdh  admin     288 Jul  7 17:16 tfe
  48 -rwxr-xr-x    1 tdh  admin   22899 Jul  7 17:16 to_pro.c
  32 -rw-r--r--    1 tdh  admin   12174 Jul  7 17:16 unix_host_common.c
 208 -rw-r--r--    1 tdh  admin  102488 Jul  7 17:16 video.c
  16 -rw-r--r--    1 tdh  admin    6512 Jul  7 17:16 win32.rc
  48 -rw-r--r--    1 tdh  admin   16938 Jul  7 17:16 win32_host_common.c
  96 -rw-r--r--    1 tdh  admin   45322 Jul  7 17:16 win32_host_fst.c
  16 -rw-r--r--    1 tdh  admin    5173 Jul  7 17:16 win32snd_driver.c
  32 -rw-r--r--    1 tdh  admin    9875 Jul  7 17:16 win_console.c
  48 -rw-r--r--    1 tdh  admin   19737 Jul  7 17:16 win_generic.c
  16 -rw-r--r--    1 tdh  admin    4634 Jul  7 17:16 win_keymap.h
  16 -rw-r--r--    1 tdh  admin    2302 Jul  7 17:16 winresource.h
  16 -rw-r--r--    1 tdh  admin     758 Jul  7 17:16 wintoolbar.bmp
  80 -rw-r--r--    1 tdh  admin   34508 Jul  7 17:16 xdriver.c
tdh@i7mac40 src % git add
Nothing specified, nothing added.
hint: Maybe you wanted to say 'git add .'?
hint: Turn this message off by running
hint: "git config advice.addEmptyPathspec false"
tdh@i7mac40 src % git add *
tdh@i7mac40 src % rm sdl2_keyboard.h
tdh@i7mac40 src % ls   
CMakeLists.txt		SDL_video.c		fix_mac_menu.m		op_routs.h		scc_windriver.c
GSplus.bat		SDL_video.h		fst.h			opcodes.x		sdl2_driver.c
INTERNALS.iwm		adb.c			glog.c			options.c		sdl2snd_driver.c
INTERNALS.overview	adb.h			glog.h			options.h		sdlsnd_driver.c
INTERNALS.xdriver	adb_keycodes.h		gsos.h			paddles.c		sim65816.c
Makefile		arch			gsport32.aps		parallel.c		size_tab.h
SDL.h			assets			gsport32.rc		parallel.rom		smartport.c
SDL_active.h		atbridge		gsportfont.h		partls.c		sound.c
SDL_audio.h		begin_code.h		headless_driver.c	printer.cpp		sound.h
SDL_cdrom.h		clock.c			host_common.c		printer.h		sound_driver.c
SDL_config.h		close_code.h		host_common.h		printer_charmaps.h	superhires.h
SDL_config_macosx.h	compile_time.c		host_fst.c		prodos.h		support.h
SDL_cpuinfo.h		config.c		host_mli.c		prodos_protos.h		tfe
SDL_endian.h		config.h		icongs.h		protos.h		to_pro.c
SDL_error.h		config.txt		imagewriter.cpp		protos_engine_c.h	unix_host_common.c
SDL_events.h		debug.c			imagewriter.h		protos_macdriver.h	video.c
SDL_joystick.h		debug.h			instable.h		protos_macsnd_driver.h	win32.rc
SDL_keyboard.h		debug_miniasm.re2c	iw_charmaps.h		protos_windriver.h	win32_host_common.c
SDL_keysym.h		debug_shell.re2c	iwm.c			protos_xdriver.h	win32_host_fst.c
SDL_loadso.h		debug_sweet16.re2c	iwm.h			rawnet			win32snd_driver.c
SDL_main.h		debug_template.re2c	iwm_35_525.h		readline.c		win_console.c
SDL_mouse.h		defc.h			joystick_driver.c	resource		win_generic.c
SDL_mutex.h		defcomm.h		macdriver_console.c	resource.h		win_keymap.h
SDL_platform.h		defs.h			macdriver_generic.c	scc.c			winresource.h
SDL_quit.h		defs_instr.h		macsnd_driver.c		scc.h			wintoolbar.bmp
SDL_rwops.h		disasm.c		make_inst		scc_imagewriter.c	xdriver.c
SDL_stdinc.h		disasm.h		make_size		scc_llap.c
SDL_thread.h		engine_c.c		make_win		scc_llap.h
SDL_timer.h		engine_s.s		mnemonics.x		scc_macdriver.c
SDL_version.h		fbdriver.c		moremem.c		scc_socket_driver.c
tdh@i7mac40 src % nano SDL_keyboard.h
tdh@i7mac40 src % nano SDL_keysym.h  
tdh@i7mac40 src % cd ../build
tdh@i7mac40 build % rm -R *
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
tdh@i7mac40 build % cmake ..;make
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:34:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keyboard.h:60:10: error: expected ';' after top level declarator
char *sym
         ^
         ;
1 error generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../SDL_keyboard.h
tdh@i7mac40 build % nano ../src/SDL_keyboard.h
tdh@i7mac40 build % rm -R *;cmake ..;make
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 'linear'
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 'linear'
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:400:3: error: implicit declaration of function 'SDL_SetTextureBlendMode' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_SetTextureBlendMode(overlay_texture, SDL_BLENDMODE_BLEND);
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(overlay_texture, &dstrect, overlay_pixels, pitch*sizeof(Uint32) );
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: note: did you mean 'SDL_CreateTexture'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:129:15: note: 'SDL_CreateTexture' declared here
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:450:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(texture, &dstrect, src_ptr, pitch*4 );
  ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
215 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_keysym.h  
tdh@i7mac40 build % nano ../src/SDL_keyboard
tdh@i7mac40 build % nano ../src/SDL_keyboard.h
tdh@i7mac40 build % rm -R *;cmake ..;make     
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:34:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keyboard.h:32:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:262:15: error: expression is not an integer constant expression
        SDLK_KP_0               = "0",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:263:15: error: expression is not an integer constant expression
        SDLK_KP_1               = "1",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:264:15: error: expression is not an integer constant expression
        SDLK_KP_2               = "2",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:265:15: error: expression is not an integer constant expression
        SDLK_KP_3               = "3",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:266:15: error: expression is not an integer constant expression
        SDLK_KP_4               = "4",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:267:15: error: expression is not an integer constant expression
        SDLK_KP_5               = "5",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:268:15: error: expression is not an integer constant expression
        SDLK_KP_6               = "6",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:269:15: error: expression is not an integer constant expression
        SDLK_KP_7               = "7",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:270:15: error: expression is not an integer constant expression
        SDLK_KP_8               = "8",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:271:15: error: expression is not an integer constant expression
        SDLK_KP_9               = "9",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:272:20: error: expression is not an integer constant expression
        SDLK_KP_PERIOD          = ".",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:273:20: error: expression is not an integer constant expression
        SDLK_KP_DIVIDE          = "/",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:274:21: error: expression is not an integer constant expression
        SDLK_KP_MULTIPLY        = "*",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:275:19: error: expression is not an integer constant expression
        SDLK_KP_MINUS           = "-",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:276:18: error: expression is not an integer constant expression
        SDLK_KP_PLUS            = "+",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:278:20: error: expression is not an integer constant expression
        SDLK_KP_EQUALS          = "=",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:279:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad0       = "0",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:280:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad1       = "1",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:281:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad2       = "2",
                                  ^~~
fatal error: too many errors emitted, stopping now [-ferror-limit=]
20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_keysym.h  
tdh@i7mac40 build % rm -R *;cmake ..;make   
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:34:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keyboard.h:32:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:279:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad0       = "0",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:280:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad1       = "1",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:281:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad2       = "2",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:282:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad3       = "3",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:283:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad4       = "4",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:284:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad5       = "5",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:285:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad6       = "6"
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:285:25: error: missing ',' between enumerators
        SDLK_ANSI_KeyPad6       = "6"
                                     ^
                                     , 
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:286:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad7       = "7",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:287:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad8       = "8",
                                  ^~~
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:288:22: error: expression is not an integer constant expression
        SDLK_ANSI_KeyPad9       = "9",
                                  ^~~
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:34:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keyboard.h:62:9: error: cannot combine with previous 'type-name' declaration specifier
        SDLKey char *sym;                       /**< SDL virtual keysym */
               ^
12 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_keysym.h
tdh@i7mac40 build % rm -R *;cmake ..;make   
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  6%] Linking C static library libx_readline.a
[  6%] Built target x_readline
[  8%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  9%] Linking C executable vmnet_helper
[  9%] Built target vmnet_helper
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/joystick_driver.c:23:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL.h:38:
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_events.h:34:
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keyboard.h:62:9: error: cannot combine with previous 'type-name' declaration specifier
        SDLKey char *sym;                       /**< SDL virtual keysym */
               ^
1 error generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/joystick_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_keyboard.h
tdh@i7mac40 build % rm -R *;cmake ..;make     
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 'linear'
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY 'linear'
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:400:3: error: implicit declaration of function 'SDL_SetTextureBlendMode' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_SetTextureBlendMode(overlay_texture, SDL_BLENDMODE_BLEND);
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(overlay_texture, &dstrect, overlay_pixels, pitch*sizeof(Uint32) );
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: note: did you mean 'SDL_CreateTexture'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:129:15: note: 'SDL_CreateTexture' declared here
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:450:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(texture, &dstrect, src_ptr, pitch*4 );
  ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
215 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/sdl2_driver.c 
tdh@i7mac40 build % rm -R *;cmake ..;make    
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  6%] Linking C executable vmnet_helper
[  6%] Built target vmnet_helper
[  8%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  9%] Linking C static library libx_readline.a
[  9%] Built target x_readline
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:115:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:116:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS', 'SDLK_UNDERSCORE' },
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:44: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:191:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:194:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:203:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:204:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:210:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:221:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  0 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected identifier or '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY "linear"
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:15: error: expected ')'
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:44:39: note: expanded from macro 'SDL_HINT_RENDER_SCALE_QUALITY'
#define SDL_HINT_RENDER_SCALE_QUALITY "linear"
                                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:382:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:400:3: error: implicit declaration of function 'SDL_SetTextureBlendMode' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_SetTextureBlendMode(overlay_texture, SDL_BLENDMODE_BLEND);
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(overlay_texture, &dstrect, overlay_pixels, pitch*sizeof(Uint32) );
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:425:3: note: did you mean 'SDL_CreateTexture'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:129:15: note: 'SDL_CreateTexture' declared here
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:450:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(texture, &dstrect, src_ptr, pitch*4 );
  ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
215 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/sdl2_driver.c
tdh@i7mac40 build % nano ../src/sdl2_driver.c
tdh@i7mac40 build % rm -R *;cmake ..;make    
zsh: sure you want to delete all 5 files in /Volumes/Data-3TB/Users/Sources/gsplus/build [yn]? y
-- The C compiler identification is AppleClang 12.0.5.12050022
-- The CXX compiler identification is AppleClang 12.0.5.12050022
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PkgConfig: /usr/local/bin/pkg-config (found version "0.29.2") 
-- Checking for module 'sdl2'
--   Found sdl2, version 2.0.14
-- Checking for module 'freetype2'
--   Found freetype2, version 23.4.17
-- Configuring done
-- Generating done
-- Build files have been written to: /Volumes/Data-3TB/Users/Sources/gsplus/build
[  1%] Building C object bin/CMakeFiles/partls.dir/partls.c.o
[  3%] Linking C executable partls
[  3%] Built target partls
[  4%] Building C object bin/CMakeFiles/x_readline.dir/readline.c.o
[  6%] Linking C static library libx_readline.a
[  6%] Built target x_readline
[  8%] Building C object bin/rawnet/CMakeFiles/vmnet_helper.dir/vmnet_helper.c.o
[  9%] Linking C executable vmnet_helper
[  9%] Built target vmnet_helper
[ 11%] Generating size_c.h, size_s.h, 8size_s.h, 16size_s.h
[ 12%] Generating 8inst_c.h, 16inst_c.h, 8inst_s.h, 16inst_s.h
[ 14%] Generating debug_miniasm.c
[ 16%] Generating debug_shell.c
[ 17%] Generating debug_sweet16.c
[ 19%] Generating debug_template.c
[ 20%] Building C object bin/CMakeFiles/GSplus.dir/adb.c.o
[ 22%] Building C object bin/CMakeFiles/GSplus.dir/clock.c.o
[ 24%] Building C object bin/CMakeFiles/GSplus.dir/config.c.o
[ 25%] Building C object bin/CMakeFiles/GSplus.dir/engine_c.c.o
[ 27%] Building C object bin/CMakeFiles/GSplus.dir/scc.c.o
[ 29%] Building C object bin/CMakeFiles/GSplus.dir/iwm.c.o
[ 30%] Building C object bin/CMakeFiles/GSplus.dir/joystick_driver.c.o
[ 32%] Building C object bin/CMakeFiles/GSplus.dir/moremem.c.o
[ 33%] Building C object bin/CMakeFiles/GSplus.dir/paddles.c.o
[ 35%] Building C object bin/CMakeFiles/GSplus.dir/parallel.c.o
[ 37%] Building CXX object bin/CMakeFiles/GSplus.dir/printer.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.cpp:2078:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
1 warning generated.
[ 38%] Building C object bin/CMakeFiles/GSplus.dir/sim65816.c.o
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/sim65816.c:13:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:307:23: warning: redefinition of typedef 'Bit8u' is a C11 feature [-Wtypedef-redefinition]
typedef unsigned char Bit8u;
                      ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/printer.h:303:23: note: previous definition is here
typedef unsigned char Bit8u;
                      ^
1 warning generated.
[ 40%] Building C object bin/CMakeFiles/GSplus.dir/smartport.c.o
[ 41%] Building C object bin/CMakeFiles/GSplus.dir/sound.c.o
[ 43%] Building C object bin/CMakeFiles/GSplus.dir/sound_driver.c.o
[ 45%] Building C object bin/CMakeFiles/GSplus.dir/video.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/video.c:916:26: warning: shifting a negative signed value is undefined [-Wshift-negative-value]
  last_line_offset = (-1 << 8) + 44;
                      ~~ ^
1 warning generated.
[ 46%] Building C object bin/CMakeFiles/GSplus.dir/scc_socket_driver.c.o
[ 48%] Building C object bin/CMakeFiles/GSplus.dir/glog.c.o
[ 50%] Building CXX object bin/CMakeFiles/GSplus.dir/imagewriter.cpp.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:102:14: warning: assigning field to itself [-Wself-assign-field]
                this->port = port;
                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:1899:10: warning: unused variable 'plane' [-Wunused-variable]
                Bit32u plane = 0;
                       ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:2215:9: warning: unused variable 'pixel' [-Wunused-variable]
        Bit32u pixel = *((Bit8u*)page->pixels + (num % page->w) + ((num / page->w) * page->pitch));
               ^
In file included from /Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.cpp:39:
/Volumes/Data-3TB/Users/Sources/gsplus/src/imagewriter.h:246:8: warning: private field 'printQuality' is not used [-Wunused-private-field]
        Bit8u printQuality;                                     // Print quality (see QUALITY_* constants)
              ^
4 warnings generated.
[ 51%] Building C object bin/CMakeFiles/GSplus.dir/scc_imagewriter.c.o
[ 53%] Building C object bin/CMakeFiles/GSplus.dir/scc_llap.c.o
[ 54%] Building C object bin/CMakeFiles/GSplus.dir/options.c.o
[ 56%] Building C object bin/CMakeFiles/GSplus.dir/disasm.c.o
[ 58%] Building C object bin/CMakeFiles/GSplus.dir/debug_shell.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1007:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1135:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1235:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:1420:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:454:12: warning: unused function 'is_jsl_e10008' [-Wunused-function]
static int is_jsl_e10008(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:458:12: warning: unused function 'is_jsl_e100a8' [-Wunused-function]
static int is_jsl_e100a8(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:464:12: warning: unused function 'is_jsl_e100b0' [-Wunused-function]
static int is_jsl_e100b0(word32 address) {
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_shell.re2c:469:12: warning: unused function 'is_jsr_bf00' [-Wunused-function]
static int is_jsr_bf00(word32 address) {
           ^
8 warnings generated.
[ 59%] Building C object bin/CMakeFiles/GSplus.dir/debug_template.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:128:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:189:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:500:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_template.re2c:118:14: warning: unused function 'ltrim' [-Wunused-function]
static char *ltrim(char *cp) {
             ^
4 warnings generated.
[ 61%] Building C object bin/CMakeFiles/GSplus.dir/debug_sweet16.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:48:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:84:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:131:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_sweet16.re2c:166:14: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
        const char *YYCTXMARKER = NULL;
                    ^
4 warnings generated.
[ 62%] Building C object bin/CMakeFiles/GSplus.dir/debug_miniasm.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:450:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:491:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:505:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:522:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:544:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/debug_miniasm.re2c:682:15: warning: unused variable 'YYCTXMARKER' [-Wunused-variable]
  const char *YYCTXMARKER = NULL;
              ^
6 warnings generated.
[ 64%] Building C object bin/CMakeFiles/GSplus.dir/host_common.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_common.c:460:27: warning: unused variable 'prefixes' [-Wunused-variable]
static struct ftype_entry prefixes[] = {
                          ^
1 warning generated.
[ 66%] Building C object bin/CMakeFiles/GSplus.dir/host_mli.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:497:12: warning: unused variable 'version' [-Wunused-variable]
  unsigned version = get_memory_c(dcb + 1, 0);
           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_mli.c:1296:10: warning: unused variable 'terr' [-Wunused-variable]
  word16 terr = 0;
         ^
2 warnings generated.
[ 67%] Building C object bin/CMakeFiles/GSplus.dir/host_fst.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:599:9: warning: unused variable 'total_size' [-Wunused-variable]
    int total_size = get_memory16_c(option_list + 0, 0);
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:671:10: warning: unused variable 'name_type' [-Wunused-variable]
  word16 name_type = get_memory16_c(pb + JudgeNameRecGS_nameType, 0);
         ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/host_fst.c:278:15: warning: unused function 'get_pstr' [-Wunused-function]
static char * get_pstr(word32 ptr) {
              ^
3 warnings generated.
[ 69%] Building C object bin/CMakeFiles/GSplus.dir/unix_host_common.c.o
[ 70%] Building C object bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Escape,             'SDLK_ESCAPE',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:117:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F1,                 'SDLK_F1',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:118:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F2,                 'SDLK_F2',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:119:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F3,                 'SDLK_F3',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:120:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F4,                 'SDLK_F4',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:121:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F5,                 'SDLK_F5',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:122:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F6,                 'SDLK_F6',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:123:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F7,                 'SDLK_F7',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:124:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F8,                 'SDLK_F8',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:125:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F9,                 'SDLK_F9',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:126:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F10,                'SDLK_F10',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:127:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F11,                'SDLK_F11',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:128:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_F12,                'SDLK_F12',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:129:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Reset,              'SDLK_PAUSE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:130:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:5: error: use of undeclared identifier 'SDLK_ANSI_Grave'
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Grave,         'SDLK_BACKQUOTE', '~' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:131:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_1,             'SDLK_1',         '!' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:132:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_2,             'SDLK_2',         '@' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:133:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_3,             'SDLK_3',         '#' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:134:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_4,             'SDLK_4',         '$' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:135:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_5,             'SDLK_5',         '%' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:136:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_6,             'SDLK_6',         '^' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:137:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_7,             'SDLK_7',         '&' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:138:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_8,             'SDLK_8',         '*' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:139:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_9,             'SDLK_9',         '(' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:140:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_0,             'SDLK_0',         ')' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:141:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Minus,         'SDLK_MINUS',    '_' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:142:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Equal,         'SDLK_EQUALS',   '=' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:143:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Delete,             'SDLK_BACKSPACE', 8 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:144:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:5: error: use of undeclared identifier 'SDLK_Help'
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Help,               'SDLK_INSERT',    0 },       /* Help? XK_Help  */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:145:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:5: error: use of undeclared identifier 'SDLK_Home'
  { SDLK_Home,               'SDLK_HOME',      0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Home,               'SDLK_HOME',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:146:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageUp,             'SDLK_PAGEUP',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:147:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:5: error: use of undeclared identifier 'SDLK_Tab'
  { SDLK_Tab,                'SDLK_TAB',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Tab,                'SDLK_TAB',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:148:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Q,             'SDLK_q',         'q' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:149:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_W,             'SDLK_w',         'w' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:150:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_E,             'SDLK_e',         'e' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:151:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_R,             'SDLK_r',         'r' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:152:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_T,             'SDLK_t',         't' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:153:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Y,             'SDLK_y',         'y' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:154:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_U,             'SDLK_u',         'u' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:155:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_I,             'SDLK_i',         'i' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:156:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_O,             'SDLK_o',         'o' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:157:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_P,             'SDLK_p',         'p' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:158:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:5: error: use of undeclared identifier 'SDLK_ANSI_LeftBracket'
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_LeftBracket,   'SDLK_LEFTBRACKET', '{' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:159:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:5: error: use of undeclared identifier 'SDLK_ANSI_RightBracket'
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_RightBracket,  'SDLK_RIGHTBRACKET', '}' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:160:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Backslash,     'SDLK_BACKSLASH', '|' },    /* backslash, bar */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:161:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:5: error: use of undeclared identifier 'SDLK_ForwardDelete'
  { SDLK_ForwardDelete,      'SDLK_DELETE',    9 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ForwardDelete,      'SDLK_DELETE',    9 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:162:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:5: error: use of undeclared identifier 'SDLK_End'
  { SDLK_End,                'SDLK_END',       0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_End,                'SDLK_END',       0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:163:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_PageDown,           'SDLK_PAGEDOWN',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:164:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_A,             'SDLK_a',         'a' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:165:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_S,             'SDLK_s',         's' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:166:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_D,             'SDLK_d',         'd' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:167:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_F,             'SDLK_f',         'f' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:168:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_G,             'SDLK_g',         'g' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:169:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_H,             'SDLK_h',         'h' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:170:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_J,             'SDLK_j',         'j' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:171:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:172:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_K,             'SDLK_k',         'kl' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_L,             'SDLK_l',         'l' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:173:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:5: error: use of undeclared identifier 'SDLK_ANSI_Semicolon'; did you mean 'SDLK_ANSI_Period'?
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
    ^~~~~~~~~~~~~~~~~~~
    SDLK_ANSI_Period
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:157:3: note: 'SDLK_ANSI_Period' declared here
        SDLK_ANSI_Period        = 46,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Semicolon,     'SDLK_SEMICOLON', 'SDLK_COLON' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:174:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:5: error: use of undeclared identifier 'SDLK_ANSI_Quote'; did you mean 'SDLK_ANSI_Q'?
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
    ^~~~~~~~~~~~~~~
    SDLK_ANSI_Q
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_keysym.h:146:2: note: 'SDLK_ANSI_Q' declared here
        SDLK_ANSI_Q             = 113,
        ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:48: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Quote,         'SDLK_QUOTE',     'SDLK_QUOTEDBL' },
                                               ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:175:48: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Return,             'SDLK_RETURN',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:176:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Shift,              'SDLK_LSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:177:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightShift,         'SDLK_RSHIFT',    0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:178:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Z,             'SDLK_z',         'z' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:179:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_X,             'SDLK_x',         'x' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:180:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_C,             'SDLK_c',         'c' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:181:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_V,             'SDLK_v',         'v' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:182:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_B,             'SDLK_b',         'b' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:183:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_N,             'SDLK_n',         'n' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:184:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_M,             'SDLK_m',         'm' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:185:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Comma,         'SDLK_COMMA',     ',' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:186:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:187:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Period,        'SDLK_PERIOD',    '.' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:187:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_ANSI_Slash,         'SDLK_SLASH',     '/' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:188:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_CapsLock,           'SDLK_CAPSLOCK',  0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:190:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:192:5: error: use of undeclared identifier 'SDLK_Control'
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:192:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:192:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:192:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_Control,            'SDLK_LCTRL',    'SDLK_LCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:192:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:5: error: use of undeclared identifier 'SDLK_RightControl'
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:47: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightControl,       'SDLK_RCTRL',    'SDLK_RCTRL' },
                                              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:193:47: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Option,             'SDLK_LALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:195:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightOption,        'SDLK_RALT',      0 },         /* Option */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:196:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:197:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_Command,            'SDLK_LGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:197:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:198:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightCommand,       'SDLK_RGUI',      0 },         /* Command */
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:198:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:5: error: use of undeclared identifier 'SDLK_SPACE'
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_SPACE,              'SDLK_SPACE',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:205:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:17: warning: multi-character character constant [-Wmultichar]
  { SDLK_LEFT,   'SDLK_LEFT',      0 },
                 ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:206:17: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_DownArrow,          'SDLK_DOWN',      0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:207:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:208:5: error: use of undeclared identifier 'SDLK_RightArrow'
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:208:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_RightArrow,         'SDLK_RIGHT',     0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:208:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:30: warning: multi-character character constant [-Wmultichar]
  { SDLK_UpArrow,            'SDLK_UP',        0 },
                             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:209:30: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_0,       'SDLK_KP_0',     '0' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:211:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_1,       'SDLK_KP_1',     '1' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:212:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_2,       'SDLK_KP_2',     '2' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:213:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_3,       'SDLK_KP_3',     '3' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:214:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_4,       'SDLK_KP_4',     '4' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:215:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_5,       'SDLK_KP_5',     '5' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:216:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_6,       'SDLK_KP_6',     '6' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:217:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_7,       'SDLK_KP_7',     '7' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:218:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:219:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_8,       'SDLK_KP_8',     '8' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:219:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:21: warning: multi-character character constant [-Wmultichar]
  {SDLK_KP_9,       'SDLK_KP_9',     '9' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:220:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MINUS,   'SDLK_KP_MINUS',  '-' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:222:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PLUS,    'SDLK_KP_PLUS',   '+' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:223:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_EQUALS,  'SDLK_KP_EQUALS', '=' }, /* Note XK_Home alias! XK_Home */
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:224:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_DIVIDE,  'SDLK_KP_DIVIDE', '/' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:225:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_MULTIPLY,'SDLK_KP_MULTIPLY', '*' },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:226:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:21: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_PERIOD, 'SDLK_KP_PERIOD', '.' },
                    ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:227:21: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:228:22: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_ENTER,   'SDLK_KP_ENTER',  13 },
                     ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:228:22: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:229:29: warning: multi-character character constant [-Wmultichar]
  { SDLK_KP_NUMLOCKCLEAR,   'SDLK_KP_NUMLOCKCLEAR', 0 }, /* Clear, XK_Clear */
                            ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:229:29: warning: character constant too long for its type
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:384:44: error: expected ')'
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
                                           ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:384:14: note: to match this '('
  SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");  // make the scaled rendering look smoother.
             ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:402:3: error: implicit declaration of function 'SDL_SetTextureBlendMode' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_SetTextureBlendMode(overlay_texture, SDL_BLENDMODE_BLEND);
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:427:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(overlay_texture, &dstrect, overlay_pixels, pitch*sizeof(Uint32) );
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:427:3: note: did you mean 'SDL_CreateTexture'?
/Volumes/Data-3TB/Users/Sources/gsplus/src/SDL_video.h:129:15: note: 'SDL_CreateTexture' declared here
SDL_Texture * SDL_CreateTexture(SDL_Renderer * renderer,
              ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:452:3: error: implicit declaration of function 'SDL_UpdateTexture' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
  SDL_UpdateTexture(texture, &dstrect, src_ptr, pitch*4 );
  ^
/Volumes/Data-3TB/Users/Sources/gsplus/src/sdl2_driver.c:511:12: error: use of undeclared identifier 'SDL_DROPFILE'
      case SDL_DROPFILE:
           ^
fatal error: too many errors emitted, stopping now [-ferror-limit=]
213 warnings and 20 errors generated.
make[2]: *** [bin/CMakeFiles/GSplus.dir/sdl2_driver.c.o] Error 1
make[1]: *** [bin/CMakeFiles/GSplus.dir/all] Error 2
make: *** [all] Error 2
tdh@i7mac40 build % nano ../src/SDL_keyboard.h

  GNU nano 2.0.6                       File: ../src/SDL_keyboard.h                                                      

/*
    SDL - Simple DirectMedia Layer
    Copyright (C) 1997-2012 Sam Lantinga

    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this library; if not, write to the Free Software
    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

    Sam Lantinga
    slouken@libsdl.org
*/

/** @file SDL_keyboard.h
 *  Include file for SDL keyboard event handling
 */

#ifndef _SDL_keyboard_h
#define _SDL_keyboard_h

#include "SDL_stdinc.h"
#include "SDL_error.h"
#include "SDL_keysym.h"

#include "begin_code.h"
/* Set up for C function definitions, even when using C++ */
#ifdef __cplusplus
extern "C" {
#endif

/** Keysym structure
 *
 *  - The scancode is hardware dependent, and should not be used by general
 *    applications.  If no hardware scancode is available, it will be 0.
 *
 *  - The 'unicode' translated character is only available when character
 *    translation is enabled by the SDL_EnableUNICODE() API.  If non-zero,
 *    this is a UNICODE character corresponding to the keypress.  If the
 *    high 9 bits of the character are 0, then this maps to the equivalent
 *    ASCII character:
 *      @code
 *      char ch;
 *      if ( (keysym.unicode & 0xFF80) == 0 ) {
 *              ch = keysym.unicode & 0x7F;
 *      } else {
 *              An international character..
 *      }
 *      @endcode
 */

typedef struct SDL_keysym {
        Uint8 scancode;                 /**< hardware specific scancode */
        SDLKey sym;                     /**< SDL virtual keysym */
        SDLMod mod;                     /**< current key modifiers */
        Uint16 unicode;                 /**< translated character */
} SDL_keysym;

/** This is the mask which refers to all hotkey bindings */
#define SDL_ALL_HOTKEYS         0xFFFFFFFF

/* Function prototypes */
/**
 * Enable/Disable UNICODE translation of keyboard input.
 *
 * This translation has some overhead, so translation defaults off.
 *
 * @param[in] enable
 * If 'enable' is 1, translation is enabled.
 * If 'enable' is 0, translation is disabled.
 * If 'enable' is -1, the translation state is not changed.
 *
                                                   [ Read 137 lines ]
^G Get Help         ^O WriteOut         ^R Read File        ^Y Prev Page        ^K Cut Text         ^C Cur Pos
^X Exit             ^J Justify          ^W Where Is         ^V Next Page        ^U UnCut Text       ^T To Spell
