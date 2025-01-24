# SDL_WriteU8

Use this function to write a byte to an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
bool SDL_WriteU8(SDL_IOStream *dst, Uint8 value);
```

## Function Parameters

|                                |           |                                               |
| ------------------------------ | --------- | --------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **dst**   | the [SDL_IOStream](SDL_IOStream) to write to. |
| Uint8                          | **value** | the byte value to write.                      |

## Return Value

(bool) Returns true on successful write or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

