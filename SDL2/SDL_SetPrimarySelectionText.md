###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.26.0.

## Related Functions

* [SDL_GetPrimarySelectionText](SDL_GetPrimarySelectionText.md)
* [SDL_HasPrimarySelectionText](SDL_HasPrimarySelectionText.md)

----
[CategoryAPI](CategoryAPI.md)
