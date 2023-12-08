###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_NumJoysticks

Count the number of joysticks attached to the system.

## Syntax

```c
int SDL_NumJoysticks(void);

```

## Return Value

Returns the number of attached joysticks on success or a negative error
code on failure; call [SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_JoystickName](SDL_JoystickName.md)
* [SDL_JoystickPath](SDL_JoystickPath.md)
* [SDL_JoystickOpen](SDL_JoystickOpen.md)

----
[CategoryAPI](CategoryAPI.md)
