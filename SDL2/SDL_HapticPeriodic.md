###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticPeriodic

A structure containing a template for a Periodic effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticPeriodic
{
    /* Header */
    Uint16 type;        /**< SDL_HAPTIC_SINE, SDL_HAPTIC_LEFTRIGHT,
                             SDL_HAPTIC_TRIANGLE, SDL_HAPTIC_SAWTOOTHUP or
                             SDL_HAPTIC_SAWTOOTHDOWN */
    SDL_HapticDirection direction;  /**< Direction of the effect. */

    /* Replay */
    Uint32 length;      /**< Duration of the effect. */
    Uint16 delay;       /**< Delay before starting the effect. */

    /* Trigger */
    Uint16 button;      /**< Button that triggers the effect. */
    Uint16 interval;    /**< How soon it can be triggered again after button. */

    /* Periodic */
    Uint16 period;      /**< Period of the wave. */
    Sint16 magnitude;   /**< Peak value; if negative, equivalent to 180 degrees extra phase shift. */
    Sint16 offset;      /**< Mean value of the wave. */
    Uint16 phase;       /**< Positive phase shift given by hundredth of a degree. */

    /* Envelope */
    Uint16 attack_length;   /**< Duration of the attack. */
    Uint16 attack_level;    /**< Level at the start of the attack. */
    Uint16 fade_length; /**< Duration of the fade. */
    Uint16 fade_level;  /**< Level at the end of the fade. */
} SDL_HapticPeriodic;
```

## Remarks

The struct handles the following effects:

- [SDL_HAPTIC_SINE](SDL_HAPTIC_SINE)
- [SDL_HAPTIC_SQUARE](SDL_HAPTIC_SQUARE)
- [SDL_HAPTIC_TRIANGLE](SDL_HAPTIC_TRIANGLE)
- [SDL_HAPTIC_SAWTOOTHUP](SDL_HAPTIC_SAWTOOTHUP)
- [SDL_HAPTIC_SAWTOOTHDOWN](SDL_HAPTIC_SAWTOOTHDOWN)

A periodic effect consists in a wave-shaped effect that repeats itself over
time. The type determines the shape of the wave and the parameters
determine the dimensions of the wave.

Phase is given by hundredth of a degree meaning that giving the phase a
value of 9000 will displace it 25% of its period. Here are sample values:

- 0: No phase displacement.
- 9000: Displaced 25% of its period.
- 18000: Displaced 50% of its period.
- 27000: Displaced 75% of its period.
- 36000: Displaced 100% of its period, same as 0, but 0 is preferred.

Examples:

```
  SDL_HAPTIC_SINE
    __      __      __      __
   /  \    /  \    /  \    /
  /    \__/    \__/    \__/

  SDL_HAPTIC_SQUARE
   __    __    __    __    __
  |  |  |  |  |  |  |  |  |  |
  |  |__|  |__|  |__|  |__|  |

  SDL_HAPTIC_TRIANGLE
    /\    /\    /\    /\    /\
   /  \  /  \  /  \  /  \  /
  /    \/    \/    \/    \/

  SDL_HAPTIC_SAWTOOTHUP
    /|  /|  /|  /|  /|  /|  /|
   / | / | / | / | / | / | / |
  /  |/  |/  |/  |/  |/  |/  |

  SDL_HAPTIC_SAWTOOTHDOWN
  \  |\  |\  |\  |\  |\  |\  |
   \ | \ | \ | \ | \ | \ | \ |
    \|  \|  \|  \|  \|  \|  \|
```

## See Also

* [SDL_HAPTIC_SINE](SDL_HAPTIC_SINE)
* [SDL_HAPTIC_LEFTRIGHT](SDL_HAPTIC_LEFTRIGHT)
* [SDL_HAPTIC_TRIANGLE](SDL_HAPTIC_TRIANGLE)
* [SDL_HAPTIC_SAWTOOTHUP](SDL_HAPTIC_SAWTOOTHUP)
* [SDL_HAPTIC_SAWTOOTHDOWN](SDL_HAPTIC_SAWTOOTHDOWN)
* [SDL_HapticEffect](SDL_HapticEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryForceFeedback](CategoryForceFeedback)


