# Introduction to SDL 2.0 


## Introduction to SDL

### What is SDL?
Simple DirectMedia Layer is a cross-platform development library designed to provide low level access to audio, keyboard, mouse, joystick, and graphics hardware via OpenGL and Direct3D. It is used by video playback software, emulators, and popular games including [Valve](http://valvesoftware.com)'s award winning catalog and many [Humble bundle](https://www.humblebundle.com) games.

SDL officially supports Windows, Mac OS X, Linux, iOS, and [Android](https://wiki.libsdl.org/SDL2/Android). Support for other platforms may be found in the source code.
> For the latest information on what is supported see <!-- http://hg.libsdl.org/SDL/file/default/docs/README-platforms.md --> [Installation](https://wiki.libsdl.org/SDL2/Installation).

SDL is written in C, works natively with C++, and there are bindings available for several other languages, including C# and Python.
> For the latest list of languages see http://www.libsdl.org/languages.php

SDL 2.0 is distributed under the [zlib license](https://zlib.net/zlib_license.html). This license allows you to use SDL freely in any software.
The Simple DirectMedia Layer library (SDL) is a general API that provides low level access to audio, keyboard, mouse, joystick, 3D hardware via OpenGL, and 2D framebuffer across multiple platforms.

### What can SDL do?
Read ahead for an overview of what SDL is capable of. If you're simply interested in the changes from 1.2 to 2.0, check out the [Migration guide](https://wiki.libsdl.org/SDL2/MigrationGuide).

***Video***

* 3D graphics:
    * SDL can be used in combination with the OpenGL API or Direct3D API for 3D graphics
    * Accelerated 2D render API:
    * Supports easy rotation, scaling and alpha blending, all accelerated using modern 3D APIs
    * Acceleration is supported using OpenGL and Direct3D, and there is a software fallback
    * Create and manage multiple windows

***Input Events***

* Events and API functions provided for:
    * Application and window state changes
    * Mouse input
    * Keyboard input
    * Joystick and game controller input
    * Multitouch gestures
    * Each event can be enabled or disabled with [SDL_EventState](https://wiki.libsdl.org/SDL2/SDL_EventState)()
    * Events are passed through a user-specified filter function before being posted to the internal event queue
    * Thread-safe event queue

***Force Feedback***

* Force feedback is supported under Windows, Mac OS X and Linux

***Audio***

* Set audio playback of 8-bit and 16-bit audio, mono stereo or 5.1 surround sound, with optional conversion if the format is not supported by the hardware
* Audio runs independently in a separate thread, filled via a user callback mechanism
* Designed for custom software audio mixers, but [http://www.libsdl.org/projects/SDL_mixer/ SDL_mixer] provides a complete audio/music output library

***File I/O Abstraction***

* General purpose abstraction for opening, reading and writing data
* Built-in support for files and memory

***Shared Object Support***

* Load shared objects (DLL on Windows, .dylib on Mac OS X, .so on Linux)
* Lookup functions in shared objects

***Threads***

* Simple thread creation API
* Simple thread local storage API
* Mutexes, semaphores and condition variables
* Atomic operations for lockless programming

***Timers***

* Get the number of milliseconds elapsed
* Wait a specified number of milliseconds
* Create timers that run alongside your code in a separate thread
* Use high resolution counter for profiling

***CPU Feature Detection***

* Query the number of CPUs
* Detect CPU features and supported instruction sets

***Endian Independence***

* Detect the endianness of the current system
* Routines for fast swapping of data values
* Read and write data of a specified endianness

***Power Management***

* Querying power management status

### What platforms does SDL run on?

* Windows:
    * Uses Win32 APIs for display, taking advantage of Direct3D for hardware acceleration
    * Uses DirectSound and XAudio2 for sound
* Mac OS X:
    * Uses Cocoa for video display, taking advantage of OpenGL for hardware acceleration
    * Uses Core Audio for sound
* Linux:
    * Uses X11 for video display, taking advantage of OpenGL for hardware acceleration
    * Uses the ALSA, OSS and PulseAudio APIs for sound
* iOS:
    * Uses UIKit for video display, taking advantage of OpenGL ES 2.0 for hardware acceleration
    * Uses Core Audio for sound
* Android
    * Uses JNI interfaces for video display, taking advantage of OpenGL ES 1.1 and 2.0 for hardware acceleration
    * Uses JNI audio callbacks for sound
    * Also see the [Android page](https://wiki.libsdl.org/SDL2/Android)

## How to get and install SDL
You can [get the source code](https://wiki.libsdl.org/SDL2/SourceCode) and [build and install it](https://wiki.libsdl.org/SDL2/Installation).

## Transitioning from SDL 1.2 to 2.0
If you used SDL 1.2 previously and you want to use SDL 2.0, please note there are some API changes and some of your code will need to be adapted.

The migration guide lists the feature differences and how to adapt old code to the new SDL 2.0:

https://wiki.libsdl.org/SDL2/MigrationGuide