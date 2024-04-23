###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_HapticDirection

Structure that represents a haptic direction.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
typedef struct SDL_HapticDirection
{
    Uint8 type;         /**< The type of encoding. */
    Sint32 dir[3];      /**< The encoded direction. */
} SDL_HapticDirection;
```

## Remarks

This is the direction where the force comes from, instead of the direction
in which the force is exerted.

Directions can be specified by: - ::[SDL_HAPTIC_POLAR](SDL_HAPTIC_POLAR) :
Specified by polar coordinates. -
::[SDL_HAPTIC_CARTESIAN](SDL_HAPTIC_CARTESIAN) : Specified by cartesian
coordinates. - ::[SDL_HAPTIC_SPHERICAL](SDL_HAPTIC_SPHERICAL) : Specified
by spherical coordinates.

Cardinal directions of the haptic device are relative to the positioning of
the device. North is considered to be away from the user.

The following diagram represents the cardinal directions:

## Code Examples

Example of force coming from the south with all encodings (force coming from the south means the user will have to pull the stick to counteract):
```c++
SDL_HapticDirection direction;

// Cartesian directions
direction.type = SDL_HAPTIC_CARTESIAN; // Using cartesian direction encoding.
direction.dir[0] = 0; // X position
direction.dir[1] = 1; // Y position
// Assuming the device has 2 axes, we don't need to specify third parameter.

// Polar directions
direction.type = SDL_HAPTIC_POLAR; // We'll be using polar direction encoding.
direction.dir[0] = 18000; // Polar only uses first parameter

// Spherical coordinates
direction.type = SDL_HAPTIC_SPHERICAL; // Spherical encoding
direction.dir[0] = 9000; // Since we only have two axes we don't need more parameters.
```

## See Also

* [SDL_HAPTIC_POLAR](SDL_HAPTIC_POLAR)
* [SDL_HAPTIC_CARTESIAN](SDL_HAPTIC_CARTESIAN)
* [SDL_HAPTIC_SPHERICAL](SDL_HAPTIC_SPHERICAL)
* [SDL_HAPTIC_STEERING_AXIS](SDL_HAPTIC_STEERING_AXIS)
* [SDL_HapticEffect](SDL_HapticEffect)
* [SDL_HapticNumAxes](SDL_HapticNumAxes)


## Data Fields

|        |          |                                                |
| ------ | -------- | ---------------------------------------------- |
| Uint8  | **type** | the type of encoding; see Remarks for details  |
| Sint32 | **dir**  | the encoded direction; see Remarks for details |
<!-- <span style="color: green;">There was a [3] attached to **dir** but I thought I remembered that we aren't including those details here.  Is that right or should I put it back in because it's important?</span> -->

## Related Structures

[SDL_HapticPeriodic](SDL_HapticPeriodic)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryForceFeedback](CategoryForceFeedback), [CategoryDraft](CategoryDraft)


