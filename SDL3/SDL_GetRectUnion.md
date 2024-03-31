###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRectUnion

Calculate the union of two rectangles.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_rect.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_GetRectUnion(const SDL_Rect * A,
                   const SDL_Rect * B,
                   SDL_Rect * result);

```

## Function Parameters

|                |                                                                                      |
| -------------- | ------------------------------------------------------------------------------------ |
| **A**          | an [SDL_Rect](SDL_Rect) structure representing the first rectangle                   |
| **B**          | an [SDL_Rect](SDL_Rect) structure representing the second rectangle                  |
| **result**     | an [SDL_Rect](SDL_Rect) structure filled in with the union of rectangles `A` and `B` |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

