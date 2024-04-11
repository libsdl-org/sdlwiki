###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WindowFlags

The flags on a window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef Uint32 SDL_WindowFlags;
```

## Remarks

These cover a lot of true/false, or on/off, window state. Some of it is
immutable after being set through [SDL_CreateWindow](SDL_CreateWindow)(),
some of it can be changed on existing windows by the app, and some of it
might be altered by the user or system outside of the app's control.

## Version

This datatype is available since SDL 3.0.0.

## See Also

* [SDL_GetWindowFlags](SDL_GetWindowFlags)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

