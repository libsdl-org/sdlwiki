# SDL_GetClipboardText

Get UTF-8 text from the clipboard.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
char * SDL_GetClipboardText(void);
```

## Return Value

(char *) Returns the clipboard text on success or an empty string on
failure; call [SDL_GetError](SDL_GetError)() for more information. This
should be freed with [SDL_free](SDL_free)() when it is no longer needed.

## Remarks

This functions returns an empty string if there was not enough memory left
for a copy of the clipboard's content.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_HasClipboardText](SDL_HasClipboardText)
- [SDL_SetClipboardText](SDL_SetClipboardText)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

