###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadS16LE

Use this function to read 16 bits of little-endian data from an [SDL_RWops](SDL_RWops.md) and return in native format.

## Syntax

```c
SDL_bool SDL_ReadS16LE(SDL_RWops *src, Sint16 *value);

```

## Function Parameters

|               |                                        |
| ------------- | -------------------------------------- |
| **src**       | the stream from which to read data     |
| **value**     | a pointer filled in with the data read |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) on successful write, [SDL_FALSE](SDL_FALSE.md) on
failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the data returned will be in
the native byte order.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
