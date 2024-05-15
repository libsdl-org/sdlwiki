###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticConstant

A structure containing a template for a Constant effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticConstant
{
    /* Header */
    Uint16 type;            /**< SDL_HAPTIC_CONSTANT */
    SDL_HapticDirection direction;  /**< Direction of the effect. */

    /* Replay */
    Uint32 length;          /**< Duration of the effect. */
    Uint16 delay;           /**< Delay before starting the effect. */

    /* Trigger */
    Uint16 button;          /**< Button that triggers the effect. */
    Uint16 interval;        /**< How soon it can be triggered again after button. */

    /* Constant */
    Sint16 level;           /**< Strength of the constant effect. */

    /* Envelope */
    Uint16 attack_length;   /**< Duration of the attack. */
    Uint16 attack_level;    /**< Level at the start of the attack. */
    Uint16 fade_length;     /**< Duration of the fade. */
    Uint16 fade_level;      /**< Level at the end of the fade. */
} SDL_HapticConstant;
```

## Remarks

This struct is exclusively for the
[SDL_HAPTIC_CONSTANT](SDL_HAPTIC_CONSTANT) effect.

A constant effect applies a constant force in the specified direction to
the joystick.

## See Also

- [SDL_HAPTIC_CONSTANT](SDL_HAPTIC_CONSTANT)
- [SDL_HapticEffect](SDL_HapticEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryHaptic](CategoryHaptic)

