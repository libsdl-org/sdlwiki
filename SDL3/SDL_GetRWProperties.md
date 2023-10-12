###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRWProperties

Get the properties associated with an [SDL_RWops](SDL_RWops).

## Syntax

```c
SDL_PropertiesID SDL_GetRWProperties(SDL_RWops *context);

```

## Function Parameters

|                 |                                                  |
| --------------- | ------------------------------------------------ |
| **context**     | a pointer to an [SDL_RWops](SDL_RWops) structure |

## Return Value

Returns a valid property ID on success or 0 on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetProperty](SDL_GetProperty)
* [SDL_SetProperty](SDL_SetProperty)

----
[CategoryAPI](CategoryAPI)

