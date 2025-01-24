# SDL_TimeFormat

The preferred time format of the current system locale.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
typedef enum SDL_TimeFormat
{
    SDL_TIME_FORMAT_24HR = 0, /**< 24 hour time */
    SDL_TIME_FORMAT_12HR = 1  /**< 12 hour time */
} SDL_TimeFormat;
```

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_GetDateTimeLocalePreferences](SDL_GetDateTimeLocalePreferences)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryTime](CategoryTime)

