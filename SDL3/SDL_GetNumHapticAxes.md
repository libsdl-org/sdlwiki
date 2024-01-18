###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumHapticAxes

Get the number of haptic axes the device has.

## Syntax

```c
int SDL_GetNumHapticAxes(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                              |
| -------------- | -------------------------------------------- |
| **haptic**     | the [SDL_Haptic](SDL_Haptic) device to query |

## Return Value

Returns the number of axes on success or a negative error code on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The number of haptic axes might be useful if working with the
[SDL_HapticDirection](SDL_HapticDirection) effect.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

