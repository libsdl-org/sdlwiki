###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetClipboardData

Get the data from clipboard for a given mime type 

## Syntax

```c
void* SDL_GetClipboardData(size_t *length, const char *mime_type);

```

## Function Parameters

|                   |                                          |
| ----------------- | ---------------------------------------- |
| **mime_type**     | The mime type to read from the clipboard |

## Return Value

Returns the retrieved data buffer or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. Caller must call
[SDL_free](SDL_free)() on the returned pointer when done with it.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetClipboardData](SDL_SetClipboardData)

----
[CategoryAPI](CategoryAPI)

