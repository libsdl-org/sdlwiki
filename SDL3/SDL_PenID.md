###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
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
pen physically leaves the area and returns, it might get a new ID.

## Version

This datatype is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryPen](CategoryPen)

