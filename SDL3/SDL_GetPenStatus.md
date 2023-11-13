###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenStatus

Retrieves the pen's current status.

## Syntax

```c
Uint32 SDL_GetPenStatus(SDL_PenID instance_id, float *x, float *y, float *axes, size_t num_axes);

```

## Function Parameters

|                     |                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **instance_id**     | The pen to query.                                                                                                     |
| **x**               | Out-mode parameter for pen x coordinate. May be NULL.                                                                 |
| **y**               | Out-mode parameter for pen y coordinate. May be NULL.                                                                 |
| **axes**            | Out-mode parameter for axis information. May be null. The axes are in the same order as ::[SDL_PenAxis](SDL_PenAxis). |
| **num_axes**        | Maximum number of axes to write to "axes".                                                                            |

## Return Value

Returns a bit mask with the current pen button states
(::[SDL_BUTTON_LMASK](SDL_BUTTON_LMASK) etc.), possibly
::[SDL_PEN_DOWN_MASK](SDL_PEN_DOWN_MASK), and exactly one of
::[SDL_PEN_INK_MASK](SDL_PEN_INK_MASK) or
::[SDL_PEN_ERASER_MASK](SDL_PEN_ERASER_MASK) , or 0 on error (see
::[SDL_GetError](SDL_GetError)()).

## Remarks

If the pen is detached (cf. ::[SDL_PenConnected](SDL_PenConnected)), this
operation may return default values.

## Version

This function is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI)

