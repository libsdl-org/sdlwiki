###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetPreferredLocales

Report the user's preferred locale.

## Header File

Defined in [<SDL3/SDL_locale.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_locale.h)

## Syntax

```c
SDL_Locale ** SDL_GetPreferredLocales(int *count);
```

## Function Parameters

|       |           |                                                                       |
| ----- | --------- | --------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of locales returned, may be NULL. |

## Return Value

([SDL_Locale](SDL_Locale) **) Returns a NULL terminated array of locale
pointers, or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information. This is a single allocation that should be freed with
[SDL_free](SDL_free)() when it is no longer needed.

## Remarks

Returned language strings are in the format xx, where 'xx' is an ISO-639
language specifier (such as "en" for English, "de" for German, etc).
Country strings are in the format YY, where "YY" is an ISO-3166 country
code (such as "US" for the United States, "CA" for Canada, etc). Country
might be NULL if there's no specific guidance on them (so you might get {
"en", "US" } for American English, but { "en", NULL } means "English
language, generically"). Language strings are never NULL, except to
terminate the array.

Please note that not all of these strings are 2 characters; some are three
or more.

The returned list of locales are in the order of the user's preference. For
example, a German citizen that is fluent in US English and knows enough
Japanese to navigate around Tokyo might have a list like: { "de", "en_US",
"jp", NULL }. Someone from England might prefer British English (where
"color" is spelled "colour", etc), but will settle for anything like it: {
"en_GB", "en", NULL }.

This function returns NULL on error, including when the platform does not
supply this information at all.

This might be a "slow" call that has to query the operating system. It's
best to ask for this once and save the results. However, this list can
change, usually because the user has changed a system preference outside of
your program; SDL will send an
[SDL_EVENT_LOCALE_CHANGED](SDL_EVENT_LOCALE_CHANGED) event in this case, if
possible, and you can call this function again to get an updated copy of
preferred locales.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLocale](CategoryLocale)

