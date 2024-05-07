###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_JoystickOpen

Open a joystick for use.

## Header File

Defined in [SDL_joystick.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_joystick.h)

## Syntax

```c
SDL_Joystick* SDL_JoystickOpen(int device_index);

```

## Function Parameters

|                      |                                    |
| -------------------- | ---------------------------------- |
| **device_index**     | the index of the joystick to query |

## Return Value

Returns a joystick identifier or NULL if an error occurred; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The `device_index` argument refers to the N'th joystick presently
recognized by SDL on the system. It is **NOT** the same as the instance ID
used to identify the joystick in future events. See
[SDL_JoystickInstanceID](SDL_JoystickInstanceID)() for more details about
instance IDs.

The joystick subsystem must be initialized before a joystick can be opened
for use.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_JoystickClose](SDL_JoystickClose)
- [SDL_JoystickInstanceID](SDL_JoystickInstanceID)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

