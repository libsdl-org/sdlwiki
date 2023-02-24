###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_IsTablet

Query if the current device is a tablet.

## Syntax

```c
SDL_bool SDL_IsTablet(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the device is a tablet,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

If SDL can't determine this, it will return [SDL_FALSE](SDL_FALSE).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

