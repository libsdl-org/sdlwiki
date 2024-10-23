###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HasClipboardText

Query whether the clipboard exists and contains a non-empty text string.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
bool SDL_HasClipboardText(void);
```

## Return Value

(bool) Returns true if the clipboard has text, or false if it does not.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetClipboardText](SDL_GetClipboardText)
- [SDL_SetClipboardText](SDL_SetClipboardText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

