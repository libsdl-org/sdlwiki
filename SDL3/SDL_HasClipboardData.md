###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HasClipboardData

Query whether there is data in the clipboard for the provided mime type.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
SDL_bool SDL_HasClipboardData(const char *mime_type);
```

## Function Parameters

|                   |                                     |
| ----------------- | ----------------------------------- |
| **mime_type**     | The mime type to check for data for |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if there exists data in clipboard for the
provided mime type, [SDL_FALSE](SDL_FALSE) if it does not.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetClipboardData](SDL_SetClipboardData)
- [SDL_GetClipboardData](SDL_GetClipboardData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

