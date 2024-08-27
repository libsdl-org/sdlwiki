###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_OutOfMemory

Set an error indicating that memory allocation failed.

## Header File

Defined in [<SDL3/SDL_error.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_error.h)

## Syntax

```c
SDL_bool SDL_OutOfMemory(void);
```

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_FALSE](SDL_FALSE).

## Remarks

This function does not do any memory allocation.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryError](CategoryError)

