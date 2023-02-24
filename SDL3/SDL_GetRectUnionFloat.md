###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRectUnionFloat

Calculate the union of two rectangles with float precision.

## Syntax

```c
int SDL_GetRectUnionFloat(const SDL_FRect * A,
                    const SDL_FRect * B,
                    SDL_FRect * result);

```

## Function Parameters

|                |                                                                                        |
| -------------- | -------------------------------------------------------------------------------------- |
| **A**          | an [SDL_FRect](SDL_FRect) structure representing the first rectangle                   |
| **B**          | an [SDL_FRect](SDL_FRect) structure representing the second rectangle                  |
| **result**     | an [SDL_FRect](SDL_FRect) structure filled in with the union of rectangles `A` and `B` |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

