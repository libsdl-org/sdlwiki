###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetClipboardText

Put UTF-8 text into the clipboard.

## Header File

Defined in [SDL_clipboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_clipboard.h)

## Syntax

```c
int SDL_SetClipboardText(const char *text);

```

## Function Parameters

|              |                                    |
| ------------ | ---------------------------------- |
| **text**     | the text to store in the clipboard |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetClipboardText](SDL_GetClipboardText)
- [SDL_HasClipboardText](SDL_HasClipboardText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

