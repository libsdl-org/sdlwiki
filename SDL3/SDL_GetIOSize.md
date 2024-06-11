###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetIOSize

Use this function to get the size of the data stream in an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
Sint64 SDL_GetIOSize(SDL_IOStream *context);
```

## Function Parameters

|                 |                                                                          |
| --------------- | ------------------------------------------------------------------------ |
| **context**     | the [SDL_IOStream](SDL_IOStream) to get the size of the data stream from |

## Return Value

Returns the size of the data stream in the [SDL_IOStream](SDL_IOStream) on
success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

