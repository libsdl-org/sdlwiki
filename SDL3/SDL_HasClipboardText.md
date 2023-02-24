###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasClipboardText

Query whether the clipboard exists and contains a non-empty text string.

## Syntax

```c
SDL_bool SDL_HasClipboardText(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the clipboard has text, or
[SDL_FALSE](SDL_FALSE) if it does not.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetClipboardText](SDL_GetClipboardText)
* [SDL_SetClipboardText](SDL_SetClipboardText)

----
[CategoryAPI](CategoryAPI), [CategoryClipboard](CategoryClipboard)


