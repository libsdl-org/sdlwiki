###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenCapabilities

Retrieves capability flags for a given [SDL_PenID](SDL_PenID).

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
SDL_PenCapabilityFlags SDL_GetPenCapabilities(SDL_PenID instance_id, SDL_PenCapabilityInfo *capabilities);
```

## Function Parameters

|                                                  |                  |                                                                          |
| ------------------------------------------------ | ---------------- | ------------------------------------------------------------------------ |
| [SDL_PenID](SDL_PenID)                           | **instance_id**  | The pen to query.                                                        |
| [SDL_PenCapabilityInfo](SDL_PenCapabilityInfo) * | **capabilities** | Detail information about pen capabilities, such as the number of buttons |

## Return Value

([SDL_PenCapabilityFlags](SDL_PenCapabilityFlags)) Returns a set of
capability flags, cf. [SDL_PEN_CAPABILITIES](SDL_PEN_CAPABILITIES)

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPen](CategoryPen)

