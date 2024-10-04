###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HasClipboardData

Query whether there is data in the clipboard for the provided mime type.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
bool SDL_HasClipboardData(const char *mime_type);
```

## Function Parameters

|              |               |                                      |
| ------------ | ------------- | ------------------------------------ |
| const char * | **mime_type** | the mime type to check for data for. |

## Return Value

(bool) Returns true if there exists data in clipboard for the provided mime
type, false if it does not.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetClipboardData](SDL_SetClipboardData)
- [SDL_GetClipboardData](SDL_GetClipboardData)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

