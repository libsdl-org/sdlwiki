###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTouchDevices

Get a list of registered touch devices.

## Header File

Defined in [<SDL3/SDL_touch.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_touch.h)

## Syntax

```c
const SDL_TouchID * SDL_GetTouchDevices(int *count);
```

## Function Parameters

|       |           |                                                                       |
| ----- | --------- | --------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of devices returned, may be NULL. |

## Return Value

(const [SDL_TouchID](SDL_TouchID) *) Returns a 0 terminated array of touch
device IDs or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

On some platforms SDL first sees the touch device if it was actually used.
Therefore the returned list might be empty, although devices are available.
After using all devices at least once the number will be correct.

This returns temporary memory which will be automatically freed later, and
can be claimed with [SDL_ClaimTemporaryMemory](SDL_ClaimTemporaryMemory)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTouch](CategoryTouch)

