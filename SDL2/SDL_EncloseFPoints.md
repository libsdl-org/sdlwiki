###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_EncloseFPoints

Calculate a minimal rectangle enclosing a set of points with float precision.

## Header File

Defined in [SDL_rect.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_rect.h)

## Syntax

```c
SDL_bool SDL_EncloseFPoints(const SDL_FPoint * points,
                        int count,
                        const SDL_FRect * clip,
                        SDL_FRect * result);
```

## Function Parameters

|                                  |            |                                                                                    |
| -------------------------------- | ---------- | ---------------------------------------------------------------------------------- |
| const [SDL_FPoint](SDL_FPoint) * | **points** | an array of [SDL_FPoint](SDL_FPoint) structures representing points to be enclosed |
| int                              | **count**  | the number of structures in the `points` array                                     |
| const [SDL_FRect](SDL_FRect) *   | **clip**   | an [SDL_FRect](SDL_FRect) used for clipping or NULL to enclose all points          |
| [SDL_FRect](SDL_FRect) *         | **result** | an [SDL_FRect](SDL_FRect) structure filled in with the minimal enclosing rectangle |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if any points were
enclosed or [SDL_FALSE](SDL_FALSE) if all the points were outside of the
clipping rectangle.

## Remarks

If `clip` is not NULL then only points inside of the clipping rectangle are
considered.

## Version

This function is available since SDL 2.0.22.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRect](CategoryRect)

