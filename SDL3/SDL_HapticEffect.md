###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HapticEffect

The generic template for any haptic effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef union SDL_HapticEffect
{
    /* Common for all force feedback effects */
    Uint16 type;                    /**< Effect type. */
    SDL_HapticConstant constant;    /**< Constant effect. */
    SDL_HapticPeriodic periodic;    /**< Periodic effect. */
    SDL_HapticCondition condition;  /**< Condition effect. */
    SDL_HapticRamp ramp;            /**< Ramp effect. */
    SDL_HapticLeftRight leftright;  /**< Left/Right effect. */
    SDL_HapticCustom custom;        /**< Custom effect. */
} SDL_HapticEffect;
```

## Remarks

All values max at 32767 (0x7FFF). Signed values also can be negative. Time
values unless specified otherwise are in milliseconds.

You can also pass [SDL_HAPTIC_INFINITY](SDL_HAPTIC_INFINITY) to length
instead of a 0-32767 value. Neither delay, interval, attack_length nor
fade_length support [SDL_HAPTIC_INFINITY](SDL_HAPTIC_INFINITY). Fade will
also not be used since effect never ends.

Additionally, the [SDL_HAPTIC_RAMP](SDL_HAPTIC_RAMP) effect does not
support a duration of [SDL_HAPTIC_INFINITY](SDL_HAPTIC_INFINITY).

Button triggers may not be supported on all devices, it is advised to not
use them if possible. Buttons start at index 1 instead of index 0 like the
joystick.

If both attack_length and fade_level are 0, the envelope is not used,
otherwise both values are used.

Common parts:

```c
 // Replay - All effects have this
 Uint32 length;        // Duration of effect (ms).
 Uint16 delay;         // Delay before starting effect.

 // Trigger - All effects have this
 Uint16 button;        // Button that triggers effect.
 Uint16 interval;      // How soon before effect can be triggered again.

 // Envelope - All effects except condition effects have this
 Uint16 attack_length; // Duration of the attack (ms).
 Uint16 attack_level;  // Level at the start of the attack.
 Uint16 fade_length;   // Duration of the fade out (ms).
 Uint16 fade_level;    // Level at the end of the fade.
```

Here we have an example of a constant effect evolution in time:

```
 Strength
 ^
 |
 |    effect level -->  _________________
 |                     /                 \
 |                    /                   \
 |                   /                     \
 |                  /                       \
 | attack_level --> |                        \
 |                  |                        |  <---  fade_level
 |
 +--------------------------------------------------> Time
                    [--]                 [---]
                    attack_length        fade_length

 [------------------][-----------------------]
 delay               length
```

Note either the attack_level or the fade_level may be above the actual
effect level.

## Version

This struct is available since SDL 3.0.0.

## See Also

* [SDL_HapticConstant](SDL_HapticConstant)
* [SDL_HapticPeriodic](SDL_HapticPeriodic)
* [SDL_HapticCondition](SDL_HapticCondition)
* [SDL_HapticRamp](SDL_HapticRamp)
* [SDL_HapticLeftRight](SDL_HapticLeftRight)
* [SDL_HapticCustom](SDL_HapticCustom)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

