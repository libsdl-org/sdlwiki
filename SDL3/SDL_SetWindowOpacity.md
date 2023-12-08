###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_SetWindowOpacity

Set the opacity for a window.

## Syntax

```c
int SDL_SetWindowOpacity(SDL_Window *window, float opacity);

```

## Function Parameters

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **window**      | the window which will be made transparent or opaque   |
| **opacity**     | the opacity value (0.0f - transparent, 1.0f - opaque) |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

The parameter `opacity` will be clamped internally between 0.0f
(transparent) and 1.0f (opaque).

This function also returns -1 if setting the opacity isn't supported.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowOpacity](SDL_GetWindowOpacity.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
