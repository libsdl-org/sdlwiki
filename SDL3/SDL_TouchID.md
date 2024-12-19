###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TouchID

A unique ID for a touch device.

## Header File

Defined in [<SDL3/SDL_touch.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h)

## Syntax

```c
typedef Uint64 SDL_TouchID;
```

## Remarks

This ID is valid for the time the device is connected to the system, and is
never reused for the lifetime of the application.

The value 0 is an invalid ID.

## Version

This datatype is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryTouch](CategoryTouch)

