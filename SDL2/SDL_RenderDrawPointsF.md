###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderDrawPointsF

Draw multiple points on the current rendering target at subpixel precision.

## Syntax

```c
int SDL_RenderDrawPointsF(SDL_Renderer * renderer,
                          const SDL_FPoint * points,
                          int count);

```

## Function Parameters

|                  |                                                 |
| ---------------- | ----------------------------------------------- |
| **renderer**     | The renderer which should draw multiple points. |
| **points**       | The points to draw                              |
| **count**        | The number of points to draw                    |

## Return Value

Return 0 on success, or -1 on error

## Version

This function is available since SDL 2.0.10.

## Example

```c
// Calculate centre of the screen

double x_centre = WIDTH / 2;
double y_centre = HEIGHT / 2;

...

// Initialize three points of triangle

SDL_FPoint a = {x_centre, y_centre};
SDL_FPoint b = {x_centre, y_centre - 10.5};
SDL_FPoint c = {x_centre - 10.5, y_centre};

// Initialize array of points

SDL_FPoint triangle[] = {
    a,
    b,
    c
};

...

// Set render color to white

SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
SDL_RenderClear(renderer);

// Draw triangle

SDL_RenderDrawPointsF(renderer, triangle, 3);

SDL_RenderPresent(renderer);

```

----
[CategoryAPI](CategoryAPI.md)
