###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TimeFormat

The preferred time format of the current system locale.

## Header File

Defined in [SDL_time.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
typedef enum SDL_TimeFormat
{
    SDL_TIME_FORMAT_24HR = 0, /**< 24 hour time */
    SDL_TIME_FORMAT_12HR = 1, /**< 12 hour time */
} SDL_TimeFormat;
```

## Version

This enum is available since SDL 3.0.0.

## See Also

* [SDL_PROP_GLOBAL_SYSTEM_TIME_FORMAT_NUMBER](SDL_PROP_GLOBAL_SYSTEM_TIME_FORMAT_NUMBER)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

