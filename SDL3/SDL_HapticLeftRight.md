# SDL_HapticLeftRight

A structure containing a template for a Left/Right effect.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticLeftRight
{
    /* Header */
    SDL_HapticEffectType type;  /**< SDL_HAPTIC_LEFTRIGHT */

    /* Replay */
    Uint32 length;          /**< Duration of the effect in milliseconds. */

    /* Rumble */
    Uint16 large_magnitude; /**< Control of the large controller motor. */
    Uint16 small_magnitude; /**< Control of the small controller motor. */
} SDL_HapticLeftRight;
```

## Remarks

This struct is exclusively for the
[SDL_HAPTIC_LEFTRIGHT](SDL_HAPTIC_LEFTRIGHT) effect.

The Left/Right effect is used to explicitly control the large and small
motors, commonly found in modern game controllers. The small (right) motor
is high frequency, and the large (left) motor is low frequency.

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_HAPTIC_LEFTRIGHT](SDL_HAPTIC_LEFTRIGHT)
- [SDL_HapticEffect](SDL_HapticEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryHaptic](CategoryHaptic)

