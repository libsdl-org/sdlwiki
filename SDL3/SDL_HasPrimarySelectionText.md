###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasPrimarySelectionText

Query whether the primary selection exists and contains a non-empty text string.

## Syntax

```c
SDL_bool SDL_HasPrimarySelectionText(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the primary selection has text, or
[SDL_FALSE](SDL_FALSE) if it does not.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetPrimarySelectionText](SDL_GetPrimarySelectionText)
* [SDL_SetPrimarySelectionText](SDL_SetPrimarySelectionText)

----
[CategoryAPI](CategoryAPI)

