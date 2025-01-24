# SDL_JoystickID

This is a unique ID for a joystick for the time it is connected to the system, and is never reused for the lifetime of the application.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
typedef Sint32 SDL_JoystickID;
```

## Remarks

If the joystick is disconnected and reconnected, it will get a new ID.

The ID value starts at 0 and increments from there. The value -1 is an
invalid ID.

## (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)



----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryJoystick](CategoryJoystick)

