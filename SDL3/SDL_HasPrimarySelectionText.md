# SDL_HasPrimarySelectionText

Query whether the primary selection exists and contains a non-empty text string.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
bool SDL_HasPrimarySelectionText(void);
```

## Return Value

(bool) Returns true if the primary selection has text, or false if it does
not.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetPrimarySelectionText](SDL_GetPrimarySelectionText)
- [SDL_SetPrimarySelectionText](SDL_SetPrimarySelectionText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

