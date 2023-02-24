###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_GetRenderTarget

Get the current render target.

## Syntax

```c
SDL_Texture* SDL_GetRenderTarget(SDL_Renderer *renderer);

```

## Function Parameters

|                  |                       |
| ---------------- | --------------------- |
| **renderer**     | the rendering context |

## Return Value

Returns the current render target or NULL for the default render target.

## Remarks

The default render target is the window for which the renderer was created,
and is reported a NULL here.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetRenderTarget](SDL_SetRenderTarget)

----
[CategoryAPI](CategoryAPI), [CategoryRender](CategoryRender), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


