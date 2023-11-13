###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenCapabilities

Retrieves capability flags for a given ::[SDL_PenID](SDL_PenID).

## Syntax

```c
Uint32 SDL_GetPenCapabilities(SDL_PenID instance_id, SDL_PenCapabilityInfo *capabilities);

```

## Function Parameters

|                     |                   |
| ------------------- | ----------------- |
| **instance_id**     | The pen to query. |

## Return Value

Returns a set of capability flags, cf. \link
[SDL_PEN_CAPABILITIES](SDL_PEN_CAPABILITIES)

## Version

This function is available since SDL 3.TBD

----
[CategoryAPI](CategoryAPI)

