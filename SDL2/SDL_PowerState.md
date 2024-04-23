###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_PowerState

The basic state for the system's power supply.

## Header File

Defined in [SDL_power.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_power.h)

## Syntax

```c
typedef enum SDL_PowerState
{
    SDL_POWERSTATE_UNKNOWN,      /**< cannot determine power status */
    SDL_POWERSTATE_ON_BATTERY,   /**< Not plugged in, running on the battery */
    SDL_POWERSTATE_NO_BATTERY,   /**< Plugged in, no battery available */
    SDL_POWERSTATE_CHARGING,     /**< Plugged in, charging battery */
    SDL_POWERSTATE_CHARGED       /**< Plugged in, battery charged */
} SDL_PowerState;
```

## Code Examples

```c++
if (SDL_GetPowerInfo(NULL, NULL) == SDL_POWERSTATE_ON_BATTERY) {
    printf("You should plug in your laptop before running this update.\n");
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryEnum](CategoryEnum), [CategoryPower](CategoryPower)


