###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

## Code Examples

```c
#include "SDL.h"

int main(int argc, char **argv)
{
    SDL_bool running = SDL_TRUE;
    SDL_Event event;
    SDL_GameController* controller = NULL;

    if (SDL_Init(SDL_INIT_EVENTS | SDL_INIT_GAMECONTROLLER | SDL_INIT_SENSOR) < 0) {
        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Error while initializing SDL2 library : %s\n", SDL_GetError());
        return 1;
    }

    while (running) {
        while (SDL_PollEvent(&event) > 0) {
            if (event.type == SDL_QUIT) {
                running = SDL_FALSE;
            }

            if (event.type == SDL_CONTROLLERDEVICEADDED) {
                controller = SDL_GameControllerOpen(event.cdevice.which);

                if (SDL_GameControllerHasSensor(controller, SDL_SENSOR_GYRO)) {
                    if (SDL_GameControllerSetSensorEnabled(controller, SDL_SENSOR_GYRO, SDL_TRUE) < 0) {
                        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't enable controller's gyroscope.");
                    }
                }

                if (SDL_GameControllerHasSensor(controller, SDL_SENSOR_ACCEL)) {
                    if (SDL_GameControllerSetSensorEnabled(controller, SDL_SENSOR_ACCEL, SDL_TRUE) < 0) {
                        SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "Couldn't enable controller's accelerometer.");
                    }
                }

                if (event.type == SDL_CONTROLLERDEVICEREMOVED) {
                    SDL_GameControllerClose(controller);
                    controller = NULL;
                }
            }
        }
    }

    SDL_GameControllerClose(controller);
    controller = NULL;

    SDL_Quit();

    return 0;
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGameController](CategoryGameController)

