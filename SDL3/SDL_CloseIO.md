###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CloseIO

Close and free an allocated [SDL_IOStream](SDL_IOStream) structure.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
int SDL_CloseIO(SDL_IOStream *context);
```

## Function Parameters

|                 |                                                 |
| --------------- | ----------------------------------------------- |
| **context**     | [SDL_IOStream](SDL_IOStream) structure to close |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

[SDL_CloseIO](SDL_CloseIO)() closes and cleans up the
[SDL_IOStream](SDL_IOStream) stream. It releases any resources used by the
stream and frees the [SDL_IOStream](SDL_IOStream) itself. This returns 0 on
success, or -1 if the stream failed to flush to its output (e.g. to disk).

Note that if this fails to flush the stream to disk, this function reports
an error, but the [SDL_IOStream](SDL_IOStream) is still invalid once this
function returns.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenIO](SDL_OpenIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

