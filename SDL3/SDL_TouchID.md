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

This datatype is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryTouch](CategoryTouch)

