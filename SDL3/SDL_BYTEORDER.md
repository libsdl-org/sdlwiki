# SDL_BYTEORDER

A macro that reports the target system's byte order.

## Header File

Defined in [<SDL3/SDL_endian.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_endian.h)

## Syntax

```c
#define SDL_BYTEORDER   SDL_LIL_ENDIAN___or_maybe___SDL_BIG_ENDIAN
```

## Remarks

This is set to either [SDL_LIL_ENDIAN](SDL_LIL_ENDIAN) or
[SDL_BIG_ENDIAN](SDL_BIG_ENDIAN) (and maybe other values in the future, if
something else becomes popular). This can be tested with the preprocessor,
so decisions can be made at compile time.

```c
#if SDL_BYTEORDER == SDL_BIG_ENDIAN
SDL_Log("This system is bigendian.");
#endif
```

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_LIL_ENDIAN](SDL_LIL_ENDIAN)
- [SDL_BIG_ENDIAN](SDL_BIG_ENDIAN)






----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryEndian](CategoryEndian)

