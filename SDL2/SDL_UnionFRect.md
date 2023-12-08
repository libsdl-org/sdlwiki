###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnionFRect

Calculate the union of two rectangles with float precision.

## Syntax

```c
void SDL_UnionFRect(const SDL_FRect * A,
                    const SDL_FRect * B,
                    SDL_FRect * result);

```

## Function Parameters

|                |                                                                                        |
| -------------- | -------------------------------------------------------------------------------------- |
| **A**          | an [SDL_FRect](SDL_FRect.md) structure representing the first rectangle                   |
| **B**          | an [SDL_FRect](SDL_FRect.md) structure representing the second rectangle                  |
| **result**     | an [SDL_FRect](SDL_FRect.md) structure filled in with the union of rectangles `A` and `B` |

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI.md)
