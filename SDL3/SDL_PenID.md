# SDL_PenID

SDL pen instance IDs.

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
typedef Uint32 SDL_PenID;
```

## Remarks

Zero is used to signify an invalid/null device.

These show up in pen events when SDL sees input from them. They remain
consistent as long as SDL can recognize a tool to be the same pen; but if a
pen's digitizer table is physically detached from the computer, it might
get a new ID when reconnected, as SDL won't know it's the same device.

These IDs are only stable within a single run of a program; the next time a
program is run, the pen's ID will likely be different, even if the hardware
hasn't been disconnected, etc.

## Version

This datatype is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryPen](CategoryPen)

