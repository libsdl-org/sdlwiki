###### (This is the legacy documentation for SDL2, the previous stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current stable version.)
# SDL_GameControllerSetSensorEnabled

Set whether data reporting for a game controller sensor is enabled.

## Header File

Defined in [SDL_gamecontroller.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_gamecontroller.h)

## Syntax

```c
int SDL_GameControllerSetSensorEnabled(SDL_GameController *gamecontroller, SDL_SensorType type, SDL_bool enabled);
```

## Function Parameters

|                                            |                    |                                           |
| ------------------------------------------ | ------------------ | ----------------------------------------- |
| [SDL_GameController](SDL_GameController) * | **gamecontroller** | The controller to update.                 |
| [SDL_SensorType](SDL_SensorType)           | **type**           | The type of sensor to enable/disable.     |
| [SDL_bool](SDL_bool)                       | **enabled**        | Whether data reporting should be enabled. |

## Return Value

(int) Returns 0 or -1 if an error occurred.

## Version

This function is available since SDL 2.0.14.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

