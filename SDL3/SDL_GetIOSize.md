# SDL_GetIOSize

Use this function to get the size of the data stream in an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
Sint64 SDL_GetIOSize(SDL_IOStream *context);
```

## Function Parameters

|                                |             |                                                                           |
| ------------------------------ | ----------- | ------------------------------------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **context** | the [SDL_IOStream](SDL_IOStream) to get the size of the data stream from. |

## Return Value

([Sint64](Sint64)) Returns the size of the data stream in the
[SDL_IOStream](SDL_IOStream) on success or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

Do not use the same [SDL_IOStream](SDL_IOStream) from two threads at once.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

