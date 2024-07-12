###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetIOProperties

Get the properties associated with an [SDL_IOStream](SDL_IOStream).

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
SDL_PropertiesID SDL_GetIOProperties(SDL_IOStream *context);
```

## Function Parameters

|                                |             |                                                         |
| ------------------------------ | ----------- | ------------------------------------------------------- |
| [SDL_IOStream](SDL_IOStream) * | **context** | a pointer to an [SDL_IOStream](SDL_IOStream) structure. |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryIOStream](CategoryIOStream)

