###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_VideoQuit

Shut down the video subsystem, if initialized with [SDL_VideoInit](SDL_VideoInit)().

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

