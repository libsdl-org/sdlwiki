###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BlendMode

A set of blend modes used in drawing operations.

## Header File

Defined in [<SDL3/SDL_blendmode.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_blendmode.h)

## Syntax

```c
typedef Uint32 SDL_BlendMode;

#define SDL_BLENDMODE_NONE                  0x00000000u /**< no blending
```

## Remarks

These predefined blend modes are supported everywhere.

Additional values may be obtained from
[SDL_ComposeCustomBlendMode](SDL_ComposeCustomBlendMode).

## Version

This datatype is available since SDL 3.0.0.

## See Also

- [SDL_ComposeCustomBlendMode](SDL_ComposeCustomBlendMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryBlendmode](CategoryBlendmode)

