###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_SetWindowBordered

Set the border state of a window.

## Syntax

```c
int SDL_SetWindowBordered(SDL_Window *window, SDL_bool bordered);

```

## Function Parameters

|                  |                                                                             |
| ---------------- | --------------------------------------------------------------------------- |
| **window**       | the window of which to change the border state                              |
| **bordered**     | [SDL_FALSE](SDL_FALSE.md) to remove border, [SDL_TRUE](SDL_TRUE.md) to add border |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_BORDERLESS`](SDL_WINDOW_BORDERLESS) flag and add or remove the
border from the actual window. This is a no-op if the window's border
already matches the requested state.

You can't change the border state of a fullscreen window.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowFlags](SDL_GetWindowFlags.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
