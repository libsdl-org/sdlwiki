###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PowerState

The basic state for the system's power supply.

## Header File

Defined in [SDL_power.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_power.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef enum SDL_PowerState
{
    SDL_POWERSTATE_ERROR = -1,   /**< error determining power status */
    SDL_POWERSTATE_UNKNOWN,      /**< cannot determine power status */
    SDL_POWERSTATE_ON_BATTERY,   /**< Not plugged in, running on the battery */
    SDL_POWERSTATE_NO_BATTERY,   /**< Plugged in, no battery available */
    SDL_POWERSTATE_CHARGING,     /**< Plugged in, charging battery */
    SDL_POWERSTATE_CHARGED       /**< Plugged in, battery charged */
} SDL_PowerState;
```

## Remarks

These are results returned by [SDL_GetPowerInfo](SDL_GetPowerInfo)().

## Version

This enum is available since SDL 3.0.0

## Code Examples

```c
if (SDL_GetPowerInfo(NULL, NULL) == SDL_POWERSTATE_ON_BATTERY) {
    SDL_Log("You should plug in your laptop before running this update.");
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

