###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_PREFERRED_LOCALES

Override for [SDL_GetPreferredLocales](SDL_GetPreferredLocales)().

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_PREFERRED_LOCALES "SDL_PREFERRED_LOCALES"
```

## Remarks

If set, this will be favored over anything the OS might report for the
user's preferred locales. Changing this hint at runtime will not generate a
[SDL_EVENT_LOCALE_CHANGED](SDL_EVENT_LOCALE_CHANGED) event (but if you can
change the hint, you can push your own event, if you want).

The format of this hint is a comma-separated list of language and locale,
combined with an underscore, as is a common format: "en_GB". Locale is
optional: "en". So you might have a list like this: "en_GB,jp,es_PT"

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

