# SDL_SetClipboardData

Offer clipboard data to the OS.

## Header File

Defined in [<SDL3/SDL_clipboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_clipboard.h)

## Syntax

```c
bool SDL_SetClipboardData(SDL_ClipboardDataCallback callback, SDL_ClipboardCleanupCallback cleanup, void *userdata, const char **mime_types, size_t num_mime_types);
```

## Function Parameters

|                                                              |                    |                                                                         |
| ------------------------------------------------------------ | ------------------ | ----------------------------------------------------------------------- |
| [SDL_ClipboardDataCallback](SDL_ClipboardDataCallback)       | **callback**       | a function pointer to the function that provides the clipboard data.    |
| [SDL_ClipboardCleanupCallback](SDL_ClipboardCleanupCallback) | **cleanup**        | a function pointer to the function that cleans up the clipboard data.   |
| void *                                                       | **userdata**       | an opaque pointer that will be forwarded to the callbacks.              |
| const char **                                                | **mime_types**     | a list of mime-types that are being offered. SDL copies the given list. |
| size_t                                                       | **num_mime_types** | the number of mime-types in the mime_types list.                        |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Tell the operating system that the application is offering clipboard data
for each of the provided mime-types. Once another application requests the
data the callback function will be called, allowing it to generate and
respond with the data for the requested mime-type.

The size of text data does not include any terminator, and the text does
not need to be null-terminated (e.g., you can directly copy a portion of a
document).

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_ClearClipboardData](SDL_ClearClipboardData)
- [SDL_GetClipboardData](SDL_GetClipboardData)
- [SDL_HasClipboardData](SDL_HasClipboardData)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryClipboard](CategoryClipboard)

