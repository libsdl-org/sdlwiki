###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetPrimarySelectionText

Put UTF-8 text into the primary selection.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
bool SDL_SetPrimarySelectionText(const char *text);
```

## Function Parameters

|              |          |                                             |
| ------------ | -------- | ------------------------------------------- |
| const char * | **text** | the text to store in the primary selection. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetPrimarySelectionText](SDL_GetPrimarySelectionText)
- [SDL_HasPrimarySelectionText](SDL_HasPrimarySelectionText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

