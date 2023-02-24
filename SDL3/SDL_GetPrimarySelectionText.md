###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPrimarySelectionText

Get UTF-8 text from the primary selection, which must be freed with [SDL_free](SDL_free)().

## Syntax

```c
char * SDL_GetPrimarySelectionText(void);

```

## Return Value

Returns the primary selection text on success or an empty string on
failure; call [SDL_GetError](SDL_GetError)() for more information. Caller
must call [SDL_free](SDL_free)() on the returned pointer when done with it
(even if there was an error).

## Remarks

This functions returns empty string if there was not enough memory left for
a copy of the primary selection's content.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasPrimarySelectionText](SDL_HasPrimarySelectionText)
* [SDL_SetPrimarySelectionText](SDL_SetPrimarySelectionText)

----
[CategoryAPI](CategoryAPI)

