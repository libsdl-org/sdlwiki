###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_IsTV

Query if the current device is a TV.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
bool SDL_IsTV(void);
```

## Return Value

(bool) Returns true if the device is a TV, false otherwise.

## Remarks

If SDL can't determine this, it will return false.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

