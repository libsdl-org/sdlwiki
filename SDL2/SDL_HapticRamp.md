###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticRamp

A structure containing a template for a Ramp effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticRamp
{
    /* Header */
    Uint16 type;            /**< ::SDL_HAPTIC_RAMP */
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

This struct is exclusively for the ::[SDL_HAPTIC_RAMP](SDL_HAPTIC_RAMP)
effect.

The ramp effect starts at start strength and ends at end strength. It
augments in linear fashion. If you use attack and fade with a ramp the
effects get added to the ramp effect making the effect become quadratic
instead of linear.

## See Also

* [SDL_HAPTIC_RAMP](SDL_HAPTIC_RAMP)
* [SDL_HapticEffect](SDL_HapticEffect)


## Data Fields

{|
|
|
|<bgcolor="#EDEDED">''Header''
|-
|Uint16
|'''type'''
|SDL_HAPTIC_RAMP
|-
|[[SDL_HapticDirection]]
|'''direction'''
|direction of the effect
|-
|
|
|<bgcolor="#EDEDED">''Replay''
|-
|Uint32
|'''length'''
|duration of the effect
|-
|Uint16
|'''delay'''
|delay before starting the effect
|-
|
|
|<bgcolor="#EDEDED">''Trigger''
|-
|Uint16
|'''button'''
|button that triggers the effect
|-
|Uint16
|'''interval'''
|how soon it can be triggered again after '''button'''
|-
|
|
|<bgcolor="#EDEDED">''Ramp''
|-
|Sint16
|'''start'''
|beginning strength level
|-
|Sint16
|'''end'''
|ending strength level
|-
|
|
|<bgcolor="#EDEDED">''Envelope''
|-
|Uint16
|'''attack_length'''
|duration of the attack
|-
|Uint16
|'''attack_level'''
|level at the start of the attack
|-
|Uint16
|'''fade_length'''
|duration of the fade
|-
|Uint16
|'''fade_level'''
|level at the end of the fade
|}

## Related Structures

:[[SDL_HapticDirection]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


