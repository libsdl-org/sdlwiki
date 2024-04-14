# FAQ: Development

## Is SDL multi-threaded?
SDL provides simple cross-platform functions for the creation of threads and synchronization using mutexes. These are used internally by SDL for some implementations of the audio subsystem and input handling.

## Can I call SDL video functions from multiple threads?
No, most graphics back ends are not thread-safe, so you should only call SDL video functions from the main thread of your application.

## Does SDL support 3D acceleration?
Yes, SDL supports 3D acceleration:
* You can use the OpenGL API or the Direct3D API in combination with SDL, for 2D and 3D graphics.
* Alternatively, you can use [SDL's 2D accelerated render API](CategoryRender) using [SDL_Texture](SDL_Texture) for pure 2D graphics which itself uses either OpenGL or Direct3D for acceleration (but it is easier to use than OpenGL/Direct3D directly and you get support for both for free).

## Does SDL support networking?
Networking is outside of the scope of SDL, but due to popular demand a simple cross-platform sockets wrapper called "SDL_net" is available at the SDL libraries page. A simple chat client/server is included which makes use of an example GUI library as well.

## Does SDL support PCX, JPG, PNG, etc...
The BMP and WAV file loaders included with SDL are simple examples demonstrating how to load an image and sound format. You should be able to write your own reader for any format. The main library is supposed to be fast and small, and so does not include any additional loaders.
A sample image loader library called "[SDL_image](https://github.com/libsdl-org/SDL_image)" is available from the SDL libraries page which supports loading BMP, PCX, GIF, JPG, PNG and TGA images to SDL surfaces.

## Does SDL support MP3, Ogg Vorbis, etc...
The BMP and WAV file loaders included with SDL are simple examples demonstrating how to load an image and sound format. You should be able to write your own reader for any format. The main library is supposed to be fast and small, and so does not include any additional loaders. A sample sound library called "[SDL_sound](https://icculus.org/SDL_sound/)" is available from the SDL libraries page which supports loading many different audio formats.

## Does SDL have text drawing support?
Games and operating systems vary widely in the type and availability of text drawing facilities. Instead of trying to deal with this in the core SDL library, there are several text drawing libraries designed for use with SDL on the SDL libraries page. Common techniques include using bitmap fonts, truetype fonts, and custom images for text.

## What kind of GUIs are there for SDL?
There are several GUI libraries available from the SDL libraries page.
There is also a demo on the SDL demos page of using GTk natively with SDL, which works really well for graphics output.
Also on the demos page is a hack written by Kent Mein using Tcl/Tk with SDL.
You may also be able to get other GUIs to work with SDL. Many of them have documentation on how to get the toolkits to work with other applications.

## Do I `#include <SDL.h>` or `#include <SDL3/SDL.h>`?

The most portable way to include SDL headers is to use angular quotes around the full header name:

```c
#include <SDL3/SDL.h>
```

This is new in SDL3! Previously, in SDL2, we recommended `#include "SDL.h"`, but this proved to be unfriendly to macOS frameworks and having the API version in the include line is useful for making dependency requirements clear.

