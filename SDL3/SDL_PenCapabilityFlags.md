###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenCapabilityFlags

Pen capabilities reported by [SDL_GetPenCapabilities](SDL_GetPenCapabilities).

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
typedef Uint32 SDL_PenCapabilityFlags;

#define SDL_PEN_DOWN_MASK          SDL_PEN_CAPABILITY(SDL_PEN_FLAG_DOWN_BIT_INDEX)   /**< Pen tip is currently touching the drawing surface. */
#define SDL_PEN_INK_MASK           SDL_PEN_CAPABILITY(SDL_PEN_FLAG_INK_BIT_INDEX)    /**< Pen has a regular drawing tip (SDL_GetPenCapabilities).  For events (SDL_PenButtonEvent, SDL_PenMotionEvent, SDL_GetPenStatus) this flag is mutually exclusive with SDL_PEN_ERASER_MASK .  */
#define SDL_PEN_ERASER_MASK        SDL_PEN_CAPABILITY(SDL_PEN_FLAG_ERASER_BIT_INDEX) /**< Pen has an eraser tip (SDL_GetPenCapabilities) or is being used as eraser (SDL_PenButtonEvent , SDL_PenMotionEvent , SDL_GetPenStatus)  */
#define SDL_PEN_AXIS_PRESSURE_MASK SDL_PEN_AXIS_CAPABILITY(SDL_PEN_AXIS_PRESSURE)    /**< Pen provides pressure information in axis SDL_PEN_AXIS_PRESSURE */
#define SDL_PEN_AXIS_XTILT_MASK    SDL_PEN_AXIS_CAPABILITY(SDL_PEN_AXIS_XTILT)       /**< Pen provides horizontal tilt information in axis SDL_PEN_AXIS_XTILT */
#define SDL_PEN_AXIS_YTILT_MASK    SDL_PEN_AXIS_CAPABILITY(SDL_PEN_AXIS_YTILT)       /**< Pen provides vertical tilt information in axis SDL_PEN_AXIS_YTILT */
#define SDL_PEN_AXIS_DISTANCE_MASK SDL_PEN_AXIS_CAPABILITY(SDL_PEN_AXIS_DISTANCE)    /**< Pen provides distance to drawing tablet in SDL_PEN_AXIS_DISTANCE */
#define SDL_PEN_AXIS_ROTATION_MASK SDL_PEN_AXIS_CAPABILITY(SDL_PEN_AXIS_ROTATION)    /**< Pen provides barrel rotation information in axis SDL_PEN_AXIS_ROTATION */
#define SDL_PEN_AXIS_SLIDER_MASK   SDL_PEN_AXIS_CAPABILITY(SDL_PEN_AXIS_SLIDER)      /**< Pen provides slider / finger wheel or similar in axis SDL_PEN_AXIS_SLIDER */
#define SDL_PEN_AXIS_BIDIRECTIONAL_MASKS (SDL_PEN_AXIS_XTILT_MASK | SDL_PEN_AXIS_YTILT_MASK)
```

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryPen](CategoryPen)

