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
country, like Canada.

Language strings are ISO-639 language specifiers (such as "en" for English,
"de" for German, etc). Country strings are ISO-3166 country codes (such as
"US" for the United States, "CA" for Canada, etc). The country might be
NULL if there's no specific guidance on them (so you might have `{ "en",
"US" }` for American English, but `{ "en", NULL }` means "English language,
generically"). Language strings are never NULL.

Please note that not all of these strings are 2 characters; some are three
or more.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_GetPreferredLocales](SDL_GetPreferredLocales)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryLocale](CategoryLocale)

