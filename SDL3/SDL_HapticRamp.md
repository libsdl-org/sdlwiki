###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HapticRamp

A structure containing a template for a Ramp effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef struct SDL_HapticRamp
{
    /* Header */
    Uint16 type;            /**< SDL_HAPTIC_RAMP */
    SDL_HapticDirection direction;  /**< Direction of the effect. */

    /* Replay */
    Uint32 length;          /**< Duration of the effect. */
    Uint16 delay;           /**< Delay before starting the effect. */

    /* Trigger */
    Uint16 button;          /**< Button that triggers the effect. */
    Uint16 interval;        /**< How soon it can be triggered again after button. */

    /* Ramp */
    Sint16 start;           /**< Beginning strength level. */
    Sint16 end;             /**< Ending strength level. */

    /* Envelope */
    Uint16 attack_length;   /**< Duration of the attack. */
    Uint16 attack_level;    /**< Level at the start of the attack. */
    Uint16 fade_length;     /**< Duration of the fade. */
    Uint16 fade_level;      /**< Level at the end of the fade. */
} SDL_HapticRamp;
```

## Remarks

This struct is exclusively for the [SDL_HAPTIC_RAMP](SDL_HAPTIC_RAMP)
effect.

The ramp effect starts at start strength and ends at end strength. It
augments in linear fashion. If you use attack and fade with a ramp the
effects get added to the ramp effect making the effect become quadratic
instead of linear.

## Version

This struct is available since SDL 3.0.0.

## See Also

* [SDL_HAPTIC_RAMP](SDL_HAPTIC_RAMP)
* [SDL_HapticEffect](SDL_HapticEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

