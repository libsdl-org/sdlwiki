###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetHaptics

Get a list of currently connected haptic devices.

## Syntax

```c
SDL_HapticID* SDL_GetHaptics(int *count);

```

## Function Parameters

|               |                                                                |
| ------------- | -------------------------------------------------------------- |
| **count**     | a pointer filled in with the number of haptic devices returned |

## Return Value

Returns a 0 terminated array of haptic device instance IDs which should be
freed with [SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_OpenHaptic](SDL_OpenHaptic)

----
[CategoryAPI](CategoryAPI)

