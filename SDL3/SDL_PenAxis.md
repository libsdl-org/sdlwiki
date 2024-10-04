###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PenAxis

Pen axis indices.

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
typedef enum SDL_PenAxis
{
    SDL_PEN_AXIS_PRESSURE,  /**< Pen pressure.  Unidirectional: 0 to 1.0 */
    SDL_PEN_AXIS_XTILT,     /**< Pen horizontal tilt angle.  Bidirectional: -90.0 to 90.0 (left-to-right). */
    SDL_PEN_AXIS_YTILT,     /**< Pen vertical tilt angle.  Bidirectional: -90.0 to 90.0 (top-to-down). */
    SDL_PEN_AXIS_DISTANCE,  /**< Pen distance to drawing surface.  Unidirectional: 0.0 to 1.0 */
    SDL_PEN_AXIS_ROTATION,  /**< Pen barrel rotation.  Bidirectional: -180 to 179.9 (clockwise, 0 is facing up, -180.0 is facing down). */
    SDL_PEN_AXIS_SLIDER,    /**< Pen finger wheel or slider (e.g., Airbrush Pen).  Unidirectional: 0 to 1.0 */
    SDL_PEN_AXIS_TANGENTIAL_PRESSURE,    /**< Pressure from squeezing the pen ("barrel pressure"). */
    SDL_PEN_AXIS_COUNT       /**< Total known pen axis types in this version of SDL. This number may grow in future releases! */
} SDL_PenAxis;
```

## Remarks

These are the valid values for the `axis` field in
[SDL_PenAxisEvent](SDL_PenAxisEvent). All axes are either normalised to
0..1 or report a (positive or negative) angle in degrees, with 0.0
representing the centre. Not all pens/backends support all axes:
unsupported axes are always zero.

To convert angles for tilt and rotation into vector representation, use
[SDL_sinf](SDL_sinf) on the XTILT, YTILT, or ROTATION component, for
example:

`SDL_sinf(xtilt * SDL_PI_F / 180.0)`.

## Version

This enum is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryPen](CategoryPen)

