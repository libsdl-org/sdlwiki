# SDL_HapticCustom

A structure containing a template for the [SDL_HAPTIC_CUSTOM](SDL_HAPTIC_CUSTOM) effect.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticCustom
{
    /* Header */
    SDL_HapticEffectType type;      /**< SDL_HAPTIC_CUSTOM */
    SDL_HapticDirection direction;  /**< Direction of the effect. */

    /* Replay */
    Uint32 length;          /**< Duration of the effect. */
    Uint16 delay;           /**< Delay before starting the effect. */

    /* Trigger */
    Uint16 button;          /**< Button that triggers the effect. */
    Uint16 interval;        /**< How soon it can be triggered again after button. */

    /* Custom */
    Uint8 channels;         /**< Axes to use, minimum of one. */
    Uint16 period;          /**< Sample periods. */
    Uint16 samples;         /**< Amount of samples. */
    Uint16 *data;           /**< Should contain channels*samples items. */

    /* Envelope */
    Uint16 attack_length;   /**< Duration of the attack. */
    Uint16 attack_level;    /**< Level at the start of the attack. */
    Uint16 fade_length;     /**< Duration of the fade. */
    Uint16 fade_level;      /**< Level at the end of the fade. */
} SDL_HapticCustom;
```

## Remarks

This struct is exclusively for the [SDL_HAPTIC_CUSTOM](SDL_HAPTIC_CUSTOM)
effect.

A custom force feedback effect is much like a periodic effect, where the
application can define its exact shape. You will have to allocate the data
yourself. Data should consist of channels * samples [Uint16](Uint16)
samples.

If channels is one, the effect is rotated using the defined direction.
Otherwise it uses the samples in data for the different axes.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_HAPTIC_CUSTOM](SDL_HAPTIC_CUSTOM)
- [SDL_HapticEffect](SDL_HapticEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryHaptic](CategoryHaptic)

