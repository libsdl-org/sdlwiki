###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticRumbleSupported

Check whether rumble is supported on a haptic device.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_bool SDL_HapticRumbleSupported(SDL_Haptic *haptic);

```

## Function Parameters

|                |                                           |
| -------------- | ----------------------------------------- |
| **haptic**     | haptic device to check for rumble support |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the effect is supported or
[SDL_FALSE](SDL_FALSE) if it isn't.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
extern SDL_Haptic* dev;
if (SDL_HapticRumbleSupported(dev)) {
    SDL_HapticRumbleInit(dev);
    SDL_HapticRumblePlay(dev, 1.0f, 3000);
    SDL_Delay(3000);
}
```

## Related Functions

* [SDL_InitHapticRumble](SDL_InitHapticRumble)

----
[CategoryAPI](CategoryAPI), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


