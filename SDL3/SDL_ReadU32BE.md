###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadU32BE

Use this function to read 32 bits of big-endian data from an [SDL_RWops](SDL_RWops) and return in native format.

## Syntax

```c
SDL_bool SDL_ReadU32BE(SDL_RWops *src, Uint32 *value);

```

## Function Parameters

|               |                                        |
| ------------- | -------------------------------------- |
| **src**       | the stream from which to read data     |
| **value**     | a pointer filled in with the data read |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) on successful write, [SDL_FALSE](SDL_FALSE) on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the data returned will be in
the native byte order.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

