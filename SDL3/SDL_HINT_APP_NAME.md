# SDL_HINT_APP_NAME

A variable setting the application name.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_APP_NAME "SDL_APP_NAME"
```

## Remarks

This hint lets you specify the application name sent to the OS when
required. For example, this will often appear in volume control applets for
audio streams, and in lists of applications which are inhibiting the
screensaver. You should use a string that describes your program ("My Game
2: The Revenge")

This will override
[SDL_PROP_APP_METADATA_NAME_STRING](SDL_PROP_APP_METADATA_NAME_STRING), if
set by the application.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

