###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_FunctionPointer

A generic function pointer.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
typedef void (*SDL_FunctionPointer)(void);
```

## Remarks

In theory, generic function pointers should use this, instead of `void *`,
since some platforms could treat code addresses differently than data
addresses. Although in current times no popular platforms make this
distinction, it is more correct and portable to use the correct type for a
generic pointer.

If for some reason you need to force this typedef to be an actual `void *`,
perhaps to work around a compiler or existing code, you can define
[`SDL_FUNCTION_POINTER_IS_VOID_POINTER`](SDL_FUNCTION_POINTER_IS_VOID_POINTER)
before including any SDL headers.

## Version

This datatype is available since SDL 3.0.0.

## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryStdinc](CategoryStdinc)

