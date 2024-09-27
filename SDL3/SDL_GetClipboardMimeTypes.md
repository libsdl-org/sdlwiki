###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetClipboardMimeTypes

Retrieve the list of mime types available in the clipboard.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
char ** SDL_GetClipboardMimeTypes(size_t *num_mime_types);
```

## Function Parameters

|          |                    |                                                              |
| -------- | ------------------ | ------------------------------------------------------------ |
| size_t * | **num_mime_types** | a pointer filled with the number of mime types, may be NULL. |

## Return Value

(char **) Returns a null terminated array of strings with mime types, or
NULL on failure; call [SDL_GetError](SDL_GetError)() for more information.
This should be freed with [SDL_free](SDL_free)() when it is no longer
needed.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetClipboardData](SDL_SetClipboardData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

