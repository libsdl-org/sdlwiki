###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenType

Retrieves the pen type for a given ::[SDL_PenID](SDL_PenID).

## Syntax

```c
SDL_PenSubtype SDL_GetPenType(SDL_PenID instance_id);

```

## Function Parameters

|                     |                   |
| ------------------- | ----------------- |
| **instance_id**     | The pen to query. |

## Return Value

Returns The corresponding pen type (cf. ::[SDL_PenSubtype](SDL_PenSubtype))
or 0 on error. Note that the pen type does not dictate whether the pen tip
is ::[SDL_PEN_TIP_INK](SDL_PEN_TIP_INK) or
::[SDL_PEN_TIP_ERASER](SDL_PEN_TIP_ERASER); to determine whether a pen is
being used for drawing or in eraser mode, check either the pen tip on
::[SDL_EVENT_PEN_DOWN](SDL_EVENT_PEN_DOWN), or the flag
::[SDL_PEN_ERASER_MASK](SDL_PEN_ERASER_MASK) in the pen state.

## Version

This function is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI)

