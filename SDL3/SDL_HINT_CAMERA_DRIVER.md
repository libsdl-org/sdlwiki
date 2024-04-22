###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_CAMERA_DRIVER

A variable that decides what camera backend to use.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_CAMERA_DRIVER "SDL_CAMERA_DRIVER"
```

## Remarks

By default, SDL will try all available camera backends in a reasonable
order until it finds one that can work, but this hint allows the app or
user to force a specific target, such as "directshow" if, say, you are on
Windows Media Foundations but want to try DirectShow instead.

The default value is unset, in which case SDL will try to figure out the
best camera backend on your behalf. This hint needs to be set before
[SDL_Init](SDL_Init)() is called to be useful.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

