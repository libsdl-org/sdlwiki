###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenType

Retrieves the pen type for a given [SDL_PenID](SDL_PenID).

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
SDL_PenSubtype SDL_GetPenType(SDL_PenID instance_id);
```

## Function Parameters

|                        |                 |                   |
| ---------------------- | --------------- | ----------------- |
| [SDL_PenID](SDL_PenID) | **instance_id** | The pen to query. |

## Return Value

([SDL_PenSubtype](SDL_PenSubtype)) Returns The corresponding pen type (cf.
[SDL_PenSubtype](SDL_PenSubtype)) or 0 on error. Note that the pen type
does not dictate whether the pen tip is [SDL_PEN_TIP_INK](SDL_PEN_TIP_INK)
or [SDL_PEN_TIP_ERASER](SDL_PEN_TIP_ERASER); to determine whether a pen is
being used for drawing or in eraser mode, check either the pen tip on
[SDL_EVENT_PEN_DOWN](SDL_EVENT_PEN_DOWN), or the flag
[SDL_PEN_ERASER_MASK](SDL_PEN_ERASER_MASK) in the pen state.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPen](CategoryPen)

