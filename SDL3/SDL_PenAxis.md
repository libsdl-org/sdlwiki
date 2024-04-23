###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenAxis

Pen axis indices

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
typedef enum SDL_PenAxis
{
    SDL_PEN_AXIS_PRESSURE = 0,               /**< Pen pressure.  Unidirectional: 0..1.0 */
    SDL_PEN_AXIS_XTILT,                      /**< Pen horizontal tilt angle.  Bidirectional: -90.0..90.0 (left-to-right).
                                                  The physical max/min tilt may be smaller than -90.0 / 90.0, cf. SDL_PenCapabilityInfo */
    SDL_PEN_AXIS_YTILT,                      /**< Pen vertical tilt angle.  Bidirectional: -90.0..90.0 (top-to-down).
                                                  The physical max/min tilt may be smaller than -90.0 / 90.0, cf. SDL_PenCapabilityInfo */
    SDL_PEN_AXIS_DISTANCE,                   /**< Pen distance to drawing surface.  Unidirectional: 0.0..1.0 */
    SDL_PEN_AXIS_ROTATION,                   /**< Pen barrel rotation.  Bidirectional: -180..179.9 (clockwise, 0 is facing up, -180.0 is facing down). */
    SDL_PEN_AXIS_SLIDER,                     /**< Pen finger wheel or slider (e.g., Airbrush Pen).  Unidirectional: 0..1.0 */
    SDL_PEN_NUM_AXES,                        /**< Last valid axis index */
    SDL_PEN_AXIS_LAST = SDL_PEN_NUM_AXES - 1 /**< Last axis index plus 1 */
} SDL_PenAxis;
```

## Remarks

Below are the valid indices to the "axis" array from
[SDL_PenMotionEvent](SDL_PenMotionEvent) and
[SDL_PenButtonEvent](SDL_PenButtonEvent). The axis indices form a
contiguous range of ints from 0 to [SDL_PEN_AXIS_LAST](SDL_PEN_AXIS_LAST),
inclusive. All "axis[]" entries are either normalised to 0..1 or report a
(positive or negative) angle in degrees, with 0.0 representing the centre.
Not all pens/backends support all axes: unsupported entries are always
"0.0f".

To convert angles for tilt and rotation into vector representation, use
[SDL_sinf](SDL_sinf) on the XTILT, YTILT, or ROTATION component, for
example:

`SDL_sinf(xtilt * SDL_PI_F / 180.0)`.

## Version

This enum is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

