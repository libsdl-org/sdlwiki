###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPenGUID

Retrieves the ::[SDL_GUID](SDL_GUID) for a given ::[SDL_PenID](SDL_PenID).

## Syntax

```c
SDL_GUID SDL_GetPenGUID(SDL_PenID instance_id);

```

## Function Parameters

|                     |                   |
| ------------------- | ----------------- |
| **instance_id**     | The pen to query. |

## Return Value

Returns The corresponding pen GUID; persistent across multiple sessions. If
"instance_id" is ::[SDL_PEN_INVALID](SDL_PEN_INVALID), returns an
all-zeroes GUID.

## Version

This function is available since SDL 3.0.0

## Related Functions

* [SDL_PenForID](SDL_PenForID)

----
[CategoryAPI](CategoryAPI)

