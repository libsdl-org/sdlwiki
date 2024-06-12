###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetClipboardData

Get the data from clipboard for a given mime type.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
void* SDL_GetClipboardData(const char *mime_type, size_t *size);
```

## Function Parameters

|              |               |                                                          |
| ------------ | ------------- | -------------------------------------------------------- |
| const char * | **mime_type** | The mime type to read from the clipboard                 |
| size_t *     | **size**      | A pointer filled in with the length of the returned data |

## Return Value

(void *) Returns the retrieved data buffer or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. Caller must call
[SDL_free](SDL_free)() on the returned pointer when done with it.

## Remarks

The size of text data does not include the terminator, but the text is
guaranteed to be null terminated.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_HasClipboardData](SDL_HasClipboardData)
- [SDL_SetClipboardData](SDL_SetClipboardData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

