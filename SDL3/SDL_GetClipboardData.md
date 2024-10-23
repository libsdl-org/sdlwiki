###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetClipboardData

Get the data from clipboard for a given mime type.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
void * SDL_GetClipboardData(const char *mime_type, size_t *size);
```

## Function Parameters

|              |               |                                                           |
| ------------ | ------------- | --------------------------------------------------------- |
| const char * | **mime_type** | the mime type to read from the clipboard.                 |
| size_t *     | **size**      | a pointer filled in with the length of the returned data. |

## Return Value

(void *) Returns the retrieved data buffer or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This should be freed
with [SDL_free](SDL_free)() when it is no longer needed.

## Remarks

The size of text data does not include the terminator, but the text is
guaranteed to be null terminated.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_HasClipboardData](SDL_HasClipboardData)
- [SDL_SetClipboardData](SDL_SetClipboardData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

