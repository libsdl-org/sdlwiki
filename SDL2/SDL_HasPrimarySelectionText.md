###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasPrimarySelectionText

Query whether the primary selection exists and contains a non-empty text string.

## Header File

Defined in [SDL_clipboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_clipboard.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_HasPrimarySelectionText(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the primary selection has text, or
[SDL_FALSE](SDL_FALSE) if it does not.

## Version

This function is available since SDL 2.26.0.

## See Also

* [SDL_GetPrimarySelectionText](SDL_GetPrimarySelectionText)
* [SDL_SetPrimarySelectionText](SDL_SetPrimarySelectionText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

