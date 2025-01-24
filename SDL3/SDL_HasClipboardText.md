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

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetClipboardText](SDL_GetClipboardText)
- [SDL_SetClipboardText](SDL_SetClipboardText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

