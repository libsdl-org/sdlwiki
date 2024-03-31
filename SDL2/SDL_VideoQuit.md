###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_VideoQuit

Shut down the video subsystem, if initialized with [SDL_VideoInit](SDL_VideoInit)().

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void SDL_VideoQuit(void);

```

## Remarks

This function closes all windows, and restores the original video mode.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_VideoInit](SDL_VideoInit)

----
[CategoryAPI](CategoryAPI)

