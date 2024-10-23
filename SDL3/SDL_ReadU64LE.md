###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ReadU64LE

Use this function to read 64 bits of little-endian data from an [SDL_IOStream](SDL_IOStream) and return in native format.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_ReadU64LE(SDL_IOStream *src, Uint64 *value);
```

## Function Parameters

|                                |           |                                         |
| ------------------------------ | --------- | --------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **src**   | the stream from which to read data.     |
| Uint64 *                       | **value** | a pointer filled in with the data read. |

## Return Value

(bool) Returns true on successful write or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

SDL byteswaps the data only if necessary, so the data returned will be in
the native byte order.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

