###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetClipboardText

Get UTF-8 text from the clipboard, which must be freed with [SDL_free](SDL_free)().

## Header File

Defined in [SDL_clipboard.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
char * SDL_GetClipboardText(void);

```

## Return Value

Returns the clipboard text on success or an empty string on failure; call
[SDL_GetError](SDL_GetError)() for more information. Caller must call
[SDL_free](SDL_free)() on the returned pointer when done with it (even if
there was an error).

## Remarks

This functions returns empty string if there was not enough memory left for
a copy of the clipboard's content.

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_HasClipboardText](SDL_HasClipboardText)
* [SDL_SetClipboardText](SDL_SetClipboardText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)


