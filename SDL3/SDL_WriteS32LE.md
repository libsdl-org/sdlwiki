###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteS32LE

Use this function to write 32 bits in native format to an [SDL_RWops](SDL_RWops.md) as little-endian data.

## Syntax

```c
SDL_bool SDL_WriteS32LE(SDL_RWops *dst, Sint32 value);

```

## Function Parameters

|               |                                          |
| ------------- | ---------------------------------------- |
| **dst**       | the stream to which data will be written |
| **value**     | the data to be written, in native format |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) on successful write, [SDL_FALSE](SDL_FALSE.md) on
failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the application always
specifies native format, and the data written will be in little-endian
format.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
