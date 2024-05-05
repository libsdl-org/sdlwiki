###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Locale

A struct to provide locale data.

## Header File

Defined in [<SDL3/SDL_locale.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_locale.h)

## Syntax

```c
typedef struct SDL_Locale
{
    const char *language;  /**< A language name, like "en" for English. */
    const char *country;  /**< A country, like "US" for America. Can be NULL. */
} SDL_Locale;
```

## Remarks

Locale data is split into a spoken language, like English, and an optional
country, like Canada. The language will be in ISO-639 format (so English
would be "en"), and the country, if not NULL, will be an ISO-3166 country
code (so Canada would be "CA").

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetPreferredLocales](SDL_GetPreferredLocales)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

