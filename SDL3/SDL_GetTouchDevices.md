###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTouchDevices

Get a list of registered touch devices.

## Header File

Defined in [SDL_touch.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_TouchID* SDL_GetTouchDevices(int *count);

```

## Function Parameters

|               |                                                                       |
| ------------- | --------------------------------------------------------------------- |
| **count**     | a pointer filled in with the number of devices returned, can be NULL. |

## Return Value

Returns a 0 terminated array of touch device IDs which should be freed with
[SDL_free](SDL_free)(), or NULL on error; call
[SDL_GetError](SDL_GetError)() for more details.

## Remarks

On some platforms SDL first sees the touch device if it was actually used.
Therefore the returned list might be empty, although devices are available.
After using all devices at least once the number will be correct.

This was fixed for Android in SDL 2.0.1.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

