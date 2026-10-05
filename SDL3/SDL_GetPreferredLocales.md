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

([SDL_Locale](SDL_Locale) **) Returns a NULL-terminated array of locale
pointers, or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information. Call [SDL_free](SDL_free)() when done with this pointer.

## Remarks

This returns a NULL-terminated array of pointers to locale information. The
returned list of locales are in the order of the user's preference. For
example, a German citizen that is fluent in US English and knows enough
Japanese to navigate around Tokyo might have a list like:

```c
{
    { "de", "DE" },
    { "en", "US" },
    { "jp", NULL },
    NULL
}
```

Someone from England might prefer British English (where "color" is spelled
"colour", etc), but will settle for anything like it:

```c
{
    { "en", "GB" },
    { "en", NULL },
    NULL
}
```

This function returns NULL on error, including when the platform does not
supply this information at all.

Note that this information is merely guidance; some platforms don't supply
it, some only supply a single language ever, some don't ever provide
country information, etc. Be prepared to receive surprising results and
plan to have fallbacks.

This might be a "slow" call that has to query the operating system. It's
best to ask for this once and save the results. However, this list can
change, usually because the user has changed a system preference outside of
your program; SDL will send an
[SDL_EVENT_LOCALE_CHANGED](SDL_EVENT_LOCALE_CHANGED) event in this case, if
possible, and you can call this function again to get an updated copy of
preferred locales.

The returned pointer is a single allocation (all the strings and structures
are allocated in a single chunk, even though they look like separate data),
and should be disposed of with a single call to [SDL_free](SDL_free)() when
it is no longer needed.

If not NULL, `*count` will be set to number of items returned, not counting
the terminating NULL pointer. `count` may be NULL if one plans to simply
iterate the returned array directly.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLocale](CategoryLocale)

