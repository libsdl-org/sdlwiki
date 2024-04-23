###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticPeriodic

A structure containing a template for a Periodic effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticPeriodic
{
    /* Header */
    Uint16 type;        /**< ::SDL_HAPTIC_SINE, ::SDL_HAPTIC_LEFTRIGHT,
                             ::SDL_HAPTIC_TRIANGLE, ::SDL_HAPTIC_SAWTOOTHUP or
                             ::SDL_HAPTIC_SAWTOOTHDOWN */
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

The struct handles the following effects: -
::[SDL_HAPTIC_SINE](SDL_HAPTIC_SINE) -
::[SDL_HAPTIC_LEFTRIGHT](SDL_HAPTIC_LEFTRIGHT) -
::[SDL_HAPTIC_TRIANGLE](SDL_HAPTIC_TRIANGLE) -
::[SDL_HAPTIC_SAWTOOTHUP](SDL_HAPTIC_SAWTOOTHUP) -
::[SDL_HAPTIC_SAWTOOTHDOWN](SDL_HAPTIC_SAWTOOTHDOWN)

A periodic effect consists in a wave-shaped effect that repeats itself over
time. The type determines the shape of the wave and the parameters
determine the dimensions of the wave.

Phase is given by hundredth of a degree meaning that giving the phase a
value of 9000 will displace it 25% of its period. Here are sample values: -
0: No phase displacement. - 9000: Displaced 25% of its period. - 18000:
Displaced 50% of its period. - 27000: Displaced 75% of its period. - 36000:
Displaced 100% of its period, same as 0, but 0 is preferred.

Examples:

## See Also

* [SDL_HAPTIC_SINE](SDL_HAPTIC_SINE)
* [SDL_HAPTIC_LEFTRIGHT](SDL_HAPTIC_LEFTRIGHT)
* [SDL_HAPTIC_TRIANGLE](SDL_HAPTIC_TRIANGLE)
* [SDL_HAPTIC_SAWTOOTHUP](SDL_HAPTIC_SAWTOOTHUP)
* [SDL_HAPTIC_SAWTOOTHDOWN](SDL_HAPTIC_SAWTOOTHDOWN)
* [SDL_HapticEffect](SDL_HapticEffect)


## Data Fields

{|
|
|
|<bgcolor="#EDEDED">''Header''
|-
|Uint16
|'''type'''
|the shape of the waves; <!-- one of the effects handled by this structure --> see Remarks for details
|-
|[SDL_HapticDirection](SDL_HapticDirection)
|'''direction'''
|direction of the effect (relative to the user)
|-
|
|
|<bgcolor="#EDEDED">''Replay''
|-
|Uint32
|'''length'''
|duration of the effect <!-- (is this the same as # of cycles? always in ms?) --> 
|-
|Uint16
|'''delay'''
|delay before starting the effect <!-- (ms?) --> 
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
|how soon it can be triggered again after '''button''' <!-- (ms?) (delay between individual waves or before the effect can be used again?) --> 
|-
|
|
|<bgcolor="#EDEDED">''Periodic''
|-
|Uint16
|'''period'''
|period of the wave <!-- (ms?) (like frequency, duration from start to start?) --> 
|-
|Sint16
|'''magnitude'''
|peak value; if negative, equivalent to 180 degrees extra phase shift <!-- (units?) (like amplitude?) --> 
|-
|Sint16
|'''offset'''
|mean value of the wave <!-- (what aspect of the wave is being offset from what other marker? Is this the distance between waves?) --> 
|-
|Uint16
|'''phase'''
|positive phase shift given by hundredth of a degree; see Remarks for details <!-- (Is this what creates the flat tops? What is the definition of a cycle, 1 sec?) --> 
|-
|
|
|<bgcolor="#EDEDED">''Envelope''
|-
|Uint16
|'''attack_length'''
|duration of the attack <!-- (ms?) --> 
|-
|Uint16
|'''attack_level'''
|level at the start of the attack <!-- (units?) --> 
|-
|Uint16
|'''fade_length'''
|duration of the fade <!-- (ms?) --> 
|-
|Uint16
|'''fade_level'''
|level at the end of the fade <!-- (units?) --> 
|}

## Related Structures

[SDL_HapticDirection](SDL_HapticDirection)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


