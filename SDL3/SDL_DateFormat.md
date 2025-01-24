# SDL_DateFormat

The preferred date format of the current system locale.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
typedef enum SDL_DateFormat
{
    SDL_DATE_FORMAT_YYYYMMDD = 0, /**< Year/Month/Day */
    SDL_DATE_FORMAT_DDMMYYYY = 1, /**< Day/Month/Year */
    SDL_DATE_FORMAT_MMDDYYYY = 2  /**< Month/Day/Year */
} SDL_DateFormat;
```

## Version

This enum is available since SDL 3.2.0.

## See Also

- [SDL_GetDateTimeLocalePreferences](SDL_GetDateTimeLocalePreferences)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryTime](CategoryTime)

