###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenName

Retrieves a human-readable description for a [SDL_PenID](SDL_PenID).

## Header File

Defined in [<SDL3/SDL_pen.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pen.h)

## Syntax

```c
const char* SDL_GetPenName(SDL_PenID instance_id);
```

## Function Parameters

|                        |                 |                   |
| ---------------------- | --------------- | ----------------- |
| [SDL_PenID](SDL_PenID) | **instance_id** | The pen to query. |

## Return Value

(const char *) Returns A string that contains the name of the pen, intended
for human consumption. The string might or might not be localised,
depending on platform settings. It is not guaranteed to be unique; use
[SDL_GetPenGUID](SDL_GetPenGUID)() for (best-effort) unique identifiers.
The pointer is managed by the SDL pen subsystem and must not be
deallocated. The pointer remains valid until SDL is shut down. Returns NULL
on error (cf. [SDL_GetError](SDL_GetError)())

## Remarks

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryPen](CategoryPen)

