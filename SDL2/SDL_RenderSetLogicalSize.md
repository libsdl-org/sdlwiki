###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RenderSetLogicalSize

Set a device independent resolution for rendering.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h)

## Syntax

```c
int SDL_RenderSetLogicalSize(SDL_Renderer * renderer, int w, int h);

```

## Function Parameters

|                  |                                                 |
| ---------------- | ----------------------------------------------- |
| **renderer**     | the renderer for which resolution should be set |
| **w**            | the width of the logical resolution             |
| **h**            | the height of the logical resolution            |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function uses the viewport and scaling functionality to allow a fixed
logical resolution for rendering, regardless of the actual output
resolution. If the actual output resolution doesn't have the same aspect
ratio the output rendering will be centered within the output display.

If the output display is a window, mouse and touch events in the window
will be filtered and scaled so they seem to arrive within the logical
resolution. The
[SDL_HINT_MOUSE_RELATIVE_SCALING](SDL_HINT_MOUSE_RELATIVE_SCALING) hint
controls whether relative motion events are also scaled.

If this function results in scaling or subpixel drawing by the rendering
backend, it will be handled using the appropriate quality hints.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_RenderGetLogicalSize](SDL_RenderGetLogicalSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

