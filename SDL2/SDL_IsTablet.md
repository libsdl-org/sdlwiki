# SDL_IsTablet

Query if the current device is a tablet.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
SDL_bool SDL_IsTablet(void);
```

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the device is a
tablet, [SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

If SDL can't determine this, it will return [SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

