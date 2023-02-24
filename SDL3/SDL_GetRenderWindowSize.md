###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetRenderWindowSize

Get the output size in screen coordinates of a rendering context.

## Syntax

```c
int SDL_GetRenderWindowSize(SDL_Renderer *renderer, int *w, int *h);

```

## Function Parameters

|                  |                                                           |
| ---------------- | --------------------------------------------------------- |
| **renderer**     | the rendering context                                     |
| **w**            | a pointer filled in with the width in screen coordinates  |
| **h**            | a pointer filled in with the height in screen coordinates |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This returns the true output size in screen coordinates, ignoring any
render targets or logical size and presentation.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetRenderer](SDL_GetRenderer)

----
[CategoryAPI](CategoryAPI)

