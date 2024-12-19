###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_FingerID

A unique ID for a single finger on a touch device.

## Header File

Defined in [<SDL3/SDL_touch.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h)

## Syntax

```c
typedef Uint64 SDL_FingerID;
```

## Remarks

This ID is valid for the time the finger (stylus, etc) is touching, and is
never reused for the lifetime of the application.

The same physical finger will have a different ID if it lifts off the touch
device and then starts a new touch, so this ID tracks the lifetime of a
single continuous touch.

The value 0 is an invalid ID.

## Version

This datatype is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryTouch](CategoryTouch)

