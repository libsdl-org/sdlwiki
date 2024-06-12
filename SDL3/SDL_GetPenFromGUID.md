###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenFromGUID

Retrieves an [SDL_PenID](SDL_PenID) for the given [SDL_GUID](SDL_GUID).

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
SDL_PenID SDL_GetPenFromGUID(SDL_GUID guid);
```

## Function Parameters

|                      |          |             |
| -------------------- | -------- | ----------- |
| [SDL_GUID](SDL_GUID) | **guid** | A pen GUID. |

## Return Value

([SDL_PenID](SDL_PenID)) Returns A valid [SDL_PenID](SDL_PenID), or
[SDL_PEN_INVALID](SDL_PEN_INVALID) if there is no matching
[SDL_PenID](SDL_PenID).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPen](CategoryPen)

