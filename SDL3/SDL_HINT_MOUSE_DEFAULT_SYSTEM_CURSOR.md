###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_MOUSE_DEFAULT_SYSTEM_CURSOR

A variable setting which system cursor to use as the default cursor.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_DEFAULT_SYSTEM_CURSOR "SDL_MOUSE_DEFAULT_SYSTEM_CURSOR"
```

## Remarks

This should be an integer corresponding to the
[SDL_SystemCursor](SDL_SystemCursor) enum. The default value is zero
([SDL_SYSTEM_CURSOR_DEFAULT](SDL_SYSTEM_CURSOR_DEFAULT)).

This hint needs to be set before [SDL_Init](SDL_Init)().

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

