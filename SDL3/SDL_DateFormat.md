###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DateFormat

The preferred date format of the current system locale.

## Header File

Defined in [SDL_time.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
typedef enum SDL_DateFormat
{
    SDL_DATE_FORMAT_YYYYMMDD = 0, /**< Year/Month/Day */
    SDL_DATE_FORMAT_DDMMYYYY = 1, /**< Day/Month/Year */
    SDL_DATE_FORMAT_MMDDYYYY = 2, /**< Month/Day/Year */
} SDL_DateFormat;
```

## Version

This enum is available since SDL 3.0.0.

## See Also

* [SDL_PROP_GLOBAL_SYSTEM_DATE_FORMAT_NUMBER](SDL_PROP_GLOBAL_SYSTEM_DATE_FORMAT_NUMBER)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

