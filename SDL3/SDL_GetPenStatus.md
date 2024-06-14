###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenStatus

Retrieves the pen's current status.

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
Uint32 SDL_GetPenStatus(SDL_PenID instance_id, float *x, float *y, float *axes, size_t num_axes);
```

## Function Parameters

|                        |                 |                                                                                                                     |
| ---------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------- |
| [SDL_PenID](SDL_PenID) | **instance_id** | the pen to query.                                                                                                   |
| float *                | **x**           | out-mode parameter for pen x coordinate. May be NULL.                                                               |
| float *                | **y**           | out-mode parameter for pen y coordinate. May be NULL.                                                               |
| float *                | **axes**        | out-mode parameter for axis information. May be null. The axes are in the same order as [SDL_PenAxis](SDL_PenAxis). |
| size_t                 | **num_axes**    | maximum number of axes to write to "axes".                                                                          |

## Return Value

(Uint32) Returns a bit mask with the current pen button states
([SDL_BUTTON_LMASK](SDL_BUTTON_LMASK) etc.), possibly
[SDL_PEN_DOWN_MASK](SDL_PEN_DOWN_MASK), and exactly one of
[SDL_PEN_INK_MASK](SDL_PEN_INK_MASK) or
[SDL_PEN_ERASER_MASK](SDL_PEN_ERASER_MASK) , or 0 on error (see
[SDL_GetError](SDL_GetError)()).

## Remarks

If the pen is detached (cf. [SDL_PenConnected](SDL_PenConnected)), this
operation may return default values.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPen](CategoryPen)

