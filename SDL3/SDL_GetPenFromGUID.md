###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenFromGUID

Retrieves an ::[SDL_PenID](SDL_PenID.md) for the given ::[SDL_GUID](SDL_GUID.md).

## Syntax

```c
SDL_PenID SDL_GetPenFromGUID(SDL_GUID guid);

```

## Function Parameters

|              |             |
| ------------ | ----------- |
| **guid**     | A pen GUID. |

## Return Value

Returns A valid ::[SDL_PenID](SDL_PenID.md), or
::[SDL_PEN_INVALID](SDL_PEN_INVALID.md) if there is no matching
[SDL_PenID](SDL_PenID.md).

## Version

This function is available since SDL 3.0.0

## Related Functions

* [SDL_GUID](SDL_GUID.md)

----
[CategoryAPI](CategoryAPI.md)
