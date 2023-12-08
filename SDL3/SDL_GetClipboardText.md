###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetClipboardText

Get UTF-8 text from the clipboard, which must be freed with [SDL_free](SDL_free.md)().

## Syntax

```c
char * SDL_GetClipboardText(void);

```

## Return Value

Returns the clipboard text on success or an empty string on failure; call
[SDL_GetError](SDL_GetError.md)() for more information. Caller must call
[SDL_free](SDL_free.md)() on the returned pointer when done with it (even if
there was an error).

## Remarks

This functions returns empty string if there was not enough memory left for
a copy of the clipboard's content.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_HasClipboardText](SDL_HasClipboardText.md)
* [SDL_SetClipboardText](SDL_SetClipboardText.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryClipboard](CategoryClipboard.md)
