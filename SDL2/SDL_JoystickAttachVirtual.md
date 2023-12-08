###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickAttachVirtual

Attach a new virtual joystick.

## Syntax

```c
int SDL_JoystickAttachVirtual(SDL_JoystickType type,
                              int naxes,
                              int nbuttons,
                              int nhats);

```

## Return Value

Returns the joystick's device index, or -1 if an error occurred.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI.md)
