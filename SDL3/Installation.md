# Installing SDL

How to install SDL varies depending on your platform. You will need to [download the source code](SourceCode) first for most of them, unless prebuilt binaries are available.

## Static linking

SDL 3.0, uses [the zlib license](FAQLicensing), which means you can build a static library linked directly to your program, or just compile SDL's C code directly as part of your project. You are completely allowed to do that. However, we encourage you to _not_ do this for various technical and moral reasons (see [README/dynapi](README/dynapi)), and won't cover the details of how to in this document.

You may not statically link SDL 1.2 in most cases due to its LGPL licensing, but you should really stop using SDL 1.2 anyhow.

## Supported platforms

### Linux/Unix

Several other platforms will be built "the Unix way," so we'll describe this platform first.

SDL supports most popular flavors of Unix: Linux, the various BSDs (FreeBSD, NetBSD, OpenBSD), Solaris, and other things like them.

First! Do you need to compile SDL yourself? It's possible your distribution's package manager already did it for you!

Debian-based systems (including Ubuntu) can simply do `sudo apt-get install libsdl3-3.0-0` to get the library installed system-wide, and all sorts of other useful dependencies, too. `sudo apt-get install libsdl3-dev` will install everything necessary to build programs that use SDL. Please see [README/linux](README/linux) for a more complete discussion of packages involved.

Red Hat-based systems (including Fedora) can simply do `sudo dnf install SDL3` to get the library installed system-wide, or `sudo dnf install SDL3-devel` to get headers and other build requirements ready for compiling your own SDL programs.

Gentoo users can `sudo emerge libsdl3` to get everything they need.

If you're compiling SDL yourself, here's what we refer to as "the Unix way" of building:

- Make sure you have build tools installed, and also [CMake](https://cmake.org).
- Get a copy of the source code, either from GitHub or an official tarball or whatever.
- Make a separate build directory (SDL will refuse to build in the base of the source tree).
- Run CMake to set things up.
- Run `make` (or maybe `ninja`) to compile SDL.
- Run `make install` (or maybe `ninja install`) to install your new SDL build on the system.

This looks something like this:


```bash
git clone https://github.com/libsdl-org/SDL
cd SDL
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --config Release --parallel
sudo cmake --install . --config Release
```

(We highly recommend [Ninja](https://ninja-build.org/) instead of `make`; add `-G Ninja` to the first `cmake` command line. But either works.)

The last command says "sudo" so we can write it to /usr/local (by default). You can change this to a different location with the `--install-prefix` option in the first call to cmake. In fact, there are a LOT of good options you can use! Try running `cmake -LAH` after the first cmake command,and look for any variables it reports that start with `SDL_`. SDL tries to do the right thing by default, though, so you can usually get away with no options at all.

Once you have the library installed, you can use the pkg-config program to help you compile your own code:

```bash
gcc -o myprogram myprogram.c `pkg-config sdl3 --cflags --libs
```

SDL on Unix should only link against the C runtime (glibc). Every thing else it needs will be dynamically loaded at runtime: X11, ALSA, d-bus, etc. This means it is possible to build an SDL that has support for all sorts of targets built in, and it will examine the system at runtime to decide what should be used (for example, if Wayland isn't available, it might try to load X11 support, etc). In that respect, if you plan to ship the SDL binary that you build, it is to your benefit to make sure your system has development headers for as many targets as possible, regardless of what you plan to personally use, so your final library is as robust as possible.

See [README/linux](README/linux) for more details.

### SteamOS

SteamOS is literally a Linux system, and uses the same binaries you distribute to generic Linux Steam users, so generally speaking, all the other Linux advice applies.

If you are shipping a Linux game on Steam, or explicitly targeting SteamOS, the system is guaranteed to provide SDL. The Steam Client will set up the dynamic loader path so that a known-good copy of SDL is available to any program that needs it before launching a game. Steam provides all major versions of SDL to date, in this manner, for both x86 and amd64, in addition to several add-on libraries like SDL_mixer. When shipping a Linux game on Steam, do not ship a build of SDL with your game. Link against SDL as normal, and expect it to be available on the player's system. This allows Valve to make fixes and improvements to their SDL and those fixes to flow on to your game.

We are obsessive about SDL3 having a backwards-compatible ABI. Whether you build your game using the Steam Runtime SDK or just about any other copy of SDL2, it _should_ work with the one that ships with Steam.

In fact, it's not a bad idea to just copy the SDL build out of the Steam Runtime if you plan to ship a Linux game for non-Steam platforms, too, since you know it's definitely well-built.

### Windows XP/Vista/7/8/10

SDL currently provides Visual Studio project files for Visual Studio 2010 or later in various flavors, and the CMake files can often generate project files for other Windows compilers. Win32 and Win64 are both supported, and we support any Windows version back to Windows XP.

The codebase is known to compile with MingW64 (both in 32 and 64 bit modes). Note that the Visual Studio builds produce standard Windows .DLLs, which are usable with any compiler that can link to them, and we care about making sure the public SDL headers work with any compiler, but making sure SDL itself builds with some of these compilers has become time-consuming and messy for diminishing returns. For simple fixes, we will always accept patches, though!

On Windows, SDL does not depend on a C runtime at all, not even for malloc(). This means it's possible to build SDL with almost any Windows compiler and have it work with a program built with any other. One .lib should work everywhere.


### macOS

You can build for macOS "the Unix way" with the CMake project files, and Xcode projects are also provided. You can ship an SDL.framework, or just build the .dylib file and ship it with an appropriate install_name to ship beside your program's binary.

If you are building "the Unix way," we encourage you to use `-DCMAKE_OSX_ARCHITECTURES=x86_64;arm64` when running CMake, so you get a "Universal" binary that runs on both Intel and Apple Silicon processors.

SDL3 has dropped support for PowerPC Macs and Mac OS X versions older than 10.9.


### Haiku OS

Build SDL "the Unix way" with the CMake project.


### iOS

SDL supports iOS 6.1+ and ships with iOS project files (in the Xcode-iOS directory) which will produce a static library. This library should be usable across all supported iOS devices (including iPhones, iPods, and iPads), and the emulator. Just load the Xcode project and click "Build."


### Android

SDL supports Android 4.1+.

See [README/android](README/android) for details on building.


### Raspberry Pi

If you want to build SDL on your Raspberry Pi directly, just build it "the Unix way," as the RPi is, more or less, a standard Linux system. It can be built with X11 support, Wayland support, and also can do OpenGL ES rendering directly to the screen without an display server, via kmsdrm, to save resources.


### Emscripten ===

SDL3 can be built with [Emscripten](https://emscripten.org/), so you can compile your SDL3-based C/C++ application to WebAssembly, and render with OpenGL ES (which becomes WebGL calls in the end).

This port is generally built "the Unix way," but with a little wrapper script over the configure script or CMake to smooth out some quirks. At the end, you should have a libSDL2.a static library to link against your Emscripten-compiled app.

Please see [README/emscripten](README/emscripten) for more details.

Also note that Emscripten has a simple implementation of SDL 1.2's API built-in. This is written by hand in JavaScript and is unrelated to the SDL codebase. The SDL3 port literally uses Emscripten to compile SDL's C code and link it to your app.


### Nintendo Switch

SDL3 runs on the Nintendo Switch! There are commercial games shipping with this port. This port is kept in a separate repository, but is available for free, under the zlib license, to anyone that is under NDA for Switch development with Nintendo. Please contact Ryan (icculus at icculus dot org) for details.

### Playstation 4 and 5

SDL3 runs on the PS4 and PS5! There are commercial games shipping with this port. This port is kept in a separate repository, but is available for free, under the zlib license, to anyone that is under NDA for Playstation development with Sony. Please contact Ryan (icculus at icculus dot org) for details.


### Microsoft GDK

(Not to be confused with [gtk+](https://gtk.org/).)

There are Visual Studio project files for GDK, which can be used to target Xbox consoles. These are in the "VisualC-GDK" directory.


### WinRT/UWP/Windows 10

There are Visual Studio project files for UWP. These are in the "VisualC-WinRT" directory.


### Windows 8/WinPhone

We no longer have build environments for Windows 8 or Windows Phone. The Win32/Win64 targets still support Windows 8.


### RISC OS

RISC OS is supported.  You can build for this platform "the unix way", or by using CMake.


### Sony PlayStation 2

The PlayStation 2 is supported using a homebrew toolkit. You can build for this platform using CMake.


### Sony PlayStation Portable

The PlayStation Portable is supported using a homebrew toolkit. You can build for this platform using CMake.


### Sony PlayStation Vita

The PlayStation Vita is supported using a homebrew toolkit. You can build for this platform using CMake.


## Not supported or abandoned

If your favorite system is listed below, we aren't working on it. If you send reasonable patches, we are happy to take a look, though!

All of these still work with SDL2, which is an incompatible API, but an option if you need to support these platforms still.

- OS/2
- QNX
- NaCL

