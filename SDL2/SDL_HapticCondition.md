###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HapticCondition

A structure containing a template for a Condition effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticCondition
{
    /* Header */
    Uint16 type;            /**< SDL_HAPTIC_SPRING, SDL_HAPTIC_DAMPER,
                                 SDL_HAPTIC_INERTIA or SDL_HAPTIC_FRICTION */
    SDL_HapticDirection direction;  /**< Direction of the effect - Not used ATM. */

    /* Replay */
    Uint32 length;          /**< Duration of the effect. */
    Uint16 delay;           /**< Delay before starting the effect. */

    /* Trigger */
    Uint16 button;          /**< Button that triggers the effect. */
    Uint16 interval;        /**< How soon it can be triggered again after button. */

    /* Condition */
    Uint16 right_sat[3];    /**< Level when joystick is to the positive side; max 0xFFFF. */
    Uint16 left_sat[3];     /**< Level when joystick is to the negative side; max 0xFFFF. */
    Sint16 right_coeff[3];  /**< How fast to increase the force towards the positive side. */
    Sint16 left_coeff[3];   /**< How fast to increase the force towards the negative side. */
    Uint16 deadband[3];     /**< Size of the dead zone; max 0xFFFF: whole axis-range when 0-centered. */
    Sint16 center[3];       /**< Position of the dead zone. */
} SDL_HapticCondition;
```

## Remarks

The struct handles the following effects:

- [SDL_HAPTIC_SPRING](SDL_HAPTIC_SPRING): Effect based on axes position.
- [SDL_HAPTIC_DAMPER](SDL_HAPTIC_DAMPER): Effect based on axes velocity.
- [SDL_HAPTIC_INERTIA](SDL_HAPTIC_INERTIA): Effect based on axes
  acceleration.
- [SDL_HAPTIC_FRICTION](SDL_HAPTIC_FRICTION): Effect based on axes
  movement.

Direction is handled by condition internals instead of a direction member.
The condition effect specific members have three parameters. The first
refers to the X axis, the second refers to the Y axis and the third refers
to the Z axis. The right terms refer to the positive side of the axis and
the left terms refer to the negative side of the axis. Please refer to the
[SDL_HapticDirection](SDL_HapticDirection) diagram for which side is
positive and which is negative.

## See Also

* [SDL_HapticDirection](SDL_HapticDirection)
* [SDL_HAPTIC_SPRING](SDL_HAPTIC_SPRING)
* [SDL_HAPTIC_DAMPER](SDL_HAPTIC_DAMPER)
* [SDL_HAPTIC_INERTIA](SDL_HAPTIC_INERTIA)
* [SDL_HAPTIC_FRICTION](SDL_HAPTIC_FRICTION)
* [SDL_HapticEffect](SDL_HapticEffect)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryForceFeedback](CategoryForceFeedback)


