###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsScreenKeyboardShown

Check whether the screen keyboard is shown for given window.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_IsScreenKeyboardShown(SDL_Window *window);

```

## Function Parameters

|                |                                                        |
| -------------- | ------------------------------------------------------ |
| **window**     | the window for which screen keyboard should be queried |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if screen keyboard is shown or
[SDL_FALSE](SDL_FALSE) if not.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_HasScreenKeyboardSupport](SDL_HasScreenKeyboardSupport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

