# SDL_HasClipboardData

Query whether there is data in the clipboard for the provided mime type.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
bool SDL_HasClipboardData(const char *mime_type);
```

## Function Parameters

|              |               |                                  |
| ------------ | ------------- | -------------------------------- |
| const char * | **mime_type** | the mime type to check for data. |

## Return Value

(bool) Returns true if data exists in the clipboard for the provided mime
type, false if it does not.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetClipboardData](SDL_SetClipboardData)
- [SDL_GetClipboardData](SDL_GetClipboardData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

