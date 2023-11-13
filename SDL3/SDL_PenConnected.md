###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PenConnected

Checks whether a pen is still attached.

## Syntax

```c
SDL_bool SDL_PenConnected(SDL_PenID instance_id);

```

## Function Parameters

|                     |           |
| ------------------- | --------- |
| **instance_id**     | A pen ID. |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if "instance_id" is valid and the
corresponding pen is attached, or [SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

If a pen is detached, it will not show up for
::[SDL_GetPens](SDL_GetPens)(). Other operations will still be available
but may return default values.

## Version

This function is available since SDL 3.0.0

----
[CategoryAPI](CategoryAPI)

