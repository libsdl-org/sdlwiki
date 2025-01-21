###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IOStream

The read/write operation structure.

## Header File

Defined in [<SDL3/SDL_iostream.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_iostream.h)

## Syntax

```c
typedef struct SDL_IOStream SDL_IOStream;
```

## Remarks

This operates as an opaque handle. There are several APIs to create various
types of I/O streams, or an app can supply an
[SDL_IOStreamInterface](SDL_IOStreamInterface) to
[SDL_OpenIO](SDL_OpenIO)() to provide their own stream implementation
behind this struct's abstract interface.

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryIOStream](CategoryIOStream)

