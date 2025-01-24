# SDL_BIG_ENDIAN

A value to represent bigendian byteorder.

## Header File

Defined in [<SDL3/SDL_endian.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_endian.h)

## Syntax

```c
#define SDL_BIG_ENDIAN  4321
```

## Remarks

This is used with the preprocessor macro [SDL_BYTEORDER](SDL_BYTEORDER), to
determine a platform's byte ordering:

```c
#if SDL_BYTEORDER == SDL_BIG_ENDIAN
SDL_Log("This system is bigendian.");
#endif
```

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_BYTEORDER](SDL_BYTEORDER)
- [SDL_LIL_ENDIAN](SDL_LIL_ENDIAN)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryEndian](CategoryEndian)

