###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenName

Retrieves a human-readable description for a ::[SDL_PenID](SDL_PenID).

## Syntax

```c
const char* SDL_GetPenName(SDL_PenID instance_id);

```

## Function Parameters

|                     |                   |
| ------------------- | ----------------- |
| **instance_id**     | The pen to query. |

## Return Value

Returns A string that contains the name of the pen, intended for human
consumption. The string might or might not be localised, depending on
platform settings. It is not guaranteed to be unique; use
::[SDL_GetPenGUID](SDL_GetPenGUID)() for (best-effort) unique identifiers.
The pointer is managed by the SDL pen subsystem and must not be
deallocated. The pointer remains valid until SDL is shut down. Returns NULL
on error (cf. ::[SDL_GetError](SDL_GetError)())

## Version

This function is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI)

