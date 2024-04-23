###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasClipboardText

Query whether the clipboard exists and contains a non-empty text string.

## Header File

Defined in [SDL_clipboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_clipboard.h)

## Syntax

```c
SDL_bool SDL_HasClipboardText(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the clipboard has text, or
[SDL_FALSE](SDL_FALSE) if it does not.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GetClipboardText](SDL_GetClipboardText)
* [SDL_SetClipboardText](SDL_SetClipboardText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

