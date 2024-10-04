###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CloseIO

Close and free an allocated [SDL_IOStream](SDL_IOStream) structure.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_CloseIO(SDL_IOStream *context);
```

## Function Parameters

|                                |             |                                                  |
| ------------------------------ | ----------- | ------------------------------------------------ |
| [SDL_IOStream](SDL_IOStream) * | **context** | [SDL_IOStream](SDL_IOStream) structure to close. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

[SDL_CloseIO](SDL_CloseIO)() closes and cleans up the
[SDL_IOStream](SDL_IOStream) stream. It releases any resources used by the
stream and frees the [SDL_IOStream](SDL_IOStream) itself. This returns true
on success, or false if the stream failed to flush to its output (e.g. to
disk).

Note that if this fails to flush the stream for any reason, this function
reports an error, but the [SDL_IOStream](SDL_IOStream) is still invalid
once this function returns.

This call flushes any buffered writes to the operating system, but there
are no guarantees that those writes have gone to physical media; they might
be in the OS's file cache, waiting to go to disk later. If it's absolutely
crucial that writes go to disk immediately, so they are definitely stored
even if the power fails before the file cache would have caught up, one
should call [SDL_FlushIO](SDL_FlushIO)() before closing. Note that flushing
takes time and makes the system and your app operate less efficiently, so
do so sparingly.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_OpenIO](SDL_OpenIO)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

