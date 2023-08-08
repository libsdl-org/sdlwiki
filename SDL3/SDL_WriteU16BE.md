###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteU16BE

Use this function to write 16 bits in native format to an [SDL_RWops](SDL_RWops) as big-endian data.

## Syntax

```c
SDL_bool SDL_WriteU16BE(SDL_RWops *dst, Uint16 value);

```

## Function Parameters

|               |                                          |
| ------------- | ---------------------------------------- |
| **dst**       | the stream to which data will be written |
| **value**     | the data to be written, in native format |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) on successful write, [SDL_FALSE](SDL_FALSE) on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the application always
specifies native format, and the data written will be in big-endian format.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

