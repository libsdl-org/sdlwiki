# SDL_DisplayID

This is a unique ID for a display for the time it is connected to the system, and is never reused for the lifetime of the application.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
typedef Uint32 SDL_DisplayID;
```

## Remarks

If the display is disconnected and reconnected, it will get a new ID.

The value 0 is an invalid ID.

## Version

This datatype is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryVideo](CategoryVideo)

