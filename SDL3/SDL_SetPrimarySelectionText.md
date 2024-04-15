###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPrimarySelectionText

Put UTF-8 text into the primary selection.

## Header File

Defined in [SDL_clipboard.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
int SDL_SetPrimarySelectionText(const char *text);

```

## Function Parameters

|              |                                            |
| ------------ | ------------------------------------------ |
| **text**     | the text to store in the primary selection |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_GetPrimarySelectionText](SDL_GetPrimarySelectionText)
* [SDL_HasPrimarySelectionText](SDL_HasPrimarySelectionText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

