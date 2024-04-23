###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticEffect

The generic template for any haptic effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

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

You can also pass ::[SDL_HAPTIC_INFINITY](SDL_HAPTIC_INFINITY) to length
instead of a 0-32767 value. Neither delay, interval, attack_length nor
fade_length support ::[SDL_HAPTIC_INFINITY](SDL_HAPTIC_INFINITY). Fade will
also not be used since effect never ends.

Additionally, the ::[SDL_HAPTIC_RAMP](SDL_HAPTIC_RAMP) effect does not
support a duration of ::[SDL_HAPTIC_INFINITY](SDL_HAPTIC_INFINITY).

Button triggers may not be supported on all devices, it is advised to not
use them if possible. Buttons start at index 1 instead of index 0 like the
joystick.

If both attack_length and fade_level are 0, the envelope is not used,
otherwise both values are used.

Common parts:

## Related Functions

* [SDL_HapticConstant](SDL_HapticConstant)
* [SDL_HapticPeriodic](SDL_HapticPeriodic)
* [SDL_HapticCondition](SDL_HapticCondition)
* [SDL_HapticRamp](SDL_HapticRamp)
* [SDL_HapticLeftRight](SDL_HapticLeftRight)
* [SDL_HapticCustom](SDL_HapticCustom)


## Data Fields

{|
|Uint16
|'''type'''
|effect type; see [[SDL_HapticPeriodic]] for details
|-
|[[SDL_HapticConstant]]
|'''constant'''
|constant effect; see [[#Remarks|Remarks]] for details
|-
|[[SDL_HapticPeriodic]]
|'''periodic'''
|periodic effect; see [[#Remarks|Remarks]] for details
|-
|[[SDL_HapticCondition]]
|'''condition'''
|condition effect; see [[#Remarks|Remarks]] for details
|-
|[[SDL_HapticRamp]]
|'''ramp'''
|ramp effect; see [[#Remarks|Remarks]] for details
|-
|[[SDL_HapticLeftRight]]
|'''leftright'''
|left/right effect; see [[#Remarks|Remarks]] for details
|-
|[[SDL_HapticCustom]]
|'''custom'''
|custom effect; see [[#Remarks|Remarks]] for details
|}

## Related Structures

:[[SDL_HapticCondition]]
:[[SDL_HapticConstant]]
:[[SDL_HapticCustom]]
:[[SDL_HapticLeftRight]]
:[[SDL_HapticPeriodic]]
:[[SDL_HapticRamp]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


