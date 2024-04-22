###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GameControllerRumble

Start a rumble effect on a game controller.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerRumble(SDL_GameController *gamecontroller, Uint16 low_frequency_rumble, Uint16 high_frequency_rumble, Uint32 duration_ms);

```

## Function Parameters

|                               |                                                                            |
| ----------------------------- | -------------------------------------------------------------------------- |
| **gamecontroller**            | The controller to vibrate                                                  |
| **low_frequency_rumble**      | The intensity of the low frequency (left) rumble motor, from 0 to 0xFFFF   |
| **high_frequency_rumble**     | The intensity of the high frequency (right) rumble motor, from 0 to 0xFFFF |
| **duration_ms**               | The duration of the rumble effect, in milliseconds                         |

## Return Value

Returns 0, or -1 if rumble isn't supported on this controller

## Remarks

Each call to this function cancels any previous rumble effect, and calling
it with 0 intensity stops any rumbling.

## Version

This function is available since SDL 2.0.9.

## See Also

* [SDL_GameControllerHasRumble](SDL_GameControllerHasRumble)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

