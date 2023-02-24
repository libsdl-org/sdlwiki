###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetPrimarySelectionText

Put UTF-8 text into the primary selection.

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

## Related Functions

* [SDL_GetPrimarySelectionText](SDL_GetPrimarySelectionText)
* [SDL_HasPrimarySelectionText](SDL_HasPrimarySelectionText)

----
[CategoryAPI](CategoryAPI)

