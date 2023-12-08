###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UnionRect

Calculate the union of two rectangles.

## Syntax

```c
void SDL_UnionRect(const SDL_Rect * A,
                   const SDL_Rect * B,
                   SDL_Rect * result);

```

## Function Parameters

|                |                                                                                      |
| -------------- | ------------------------------------------------------------------------------------ |
| **A**          | an [SDL_Rect](SDL_Rect.md) structure representing the first rectangle                   |
| **B**          | an [SDL_Rect](SDL_Rect.md) structure representing the second rectangle                  |
| **result**     | an [SDL_Rect](SDL_Rect.md) structure filled in with the union of rectangles `A` and `B` |

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
