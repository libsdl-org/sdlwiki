###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGStructures for details on editing this page*^*^*^*^* -->
# SDL_HapticLeftRight

A structure containing a template for a Left/Right effect.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticLeftRight
{
    /* Header */
    Uint16 type;            /**< ::SDL_HAPTIC_LEFTRIGHT */

    /* Replay */
    Uint32 length;          /**< Duration of the effect in milliseconds. */

    /* Rumble */
    Uint16 large_magnitude; /**< Control of the large controller motor. */
    Uint16 small_magnitude; /**< Control of the small controller motor. */
} SDL_HapticLeftRight;
```

## Remarks

This struct is exclusively for the
::[SDL_HAPTIC_LEFTRIGHT](SDL_HAPTIC_LEFTRIGHT) effect.

The Left/Right effect is used to explicitly control the large and small
motors, commonly found in modern game controllers. The small (right) motor
is high frequency, and the large (left) motor is low frequency.

## See Also

* [SDL_HAPTIC_LEFTRIGHT](SDL_HAPTIC_LEFTRIGHT)
* [SDL_HapticEffect](SDL_HapticEffect)


## Data Fields

{|
|
|
|<bgcolor="#EDEDED">''Header''
|-
|Uint16
|'''type'''
|SDL_HAPTIC_LEFTRIGHT
|-
|
|
|<bgcolor="#EDEDED">''Replay''
|-
|Uint32
|'''length'''
|duration of the effect
|-
|
|
|<bgcolor="#EDEDED">''Rumble''
|-
|Uint16
|'''large_magnitude'''
|control of the large controller motor
|-
|Uint16
|'''small_magnitude'''
|control of the small controller motor
|}

## Related Structures

:[[SDL_HapticEffect]]

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


