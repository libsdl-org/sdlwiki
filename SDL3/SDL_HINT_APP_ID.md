###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_APP_ID

A variable setting the app ID string.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_APP_ID      "SDL_APP_ID"
```

## Remarks

This string is used by desktop compositors to identify and group windows
together, as well as match applications with associated desktop settings
and icons.

This will override
[SDL_PROP_APP_METADATA_IDENTIFIER_STRING](SDL_PROP_APP_METADATA_IDENTIFIER_STRING),
if set by the application.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

