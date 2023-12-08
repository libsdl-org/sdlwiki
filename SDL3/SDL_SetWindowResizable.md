###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_SetWindowResizable

Set the user-resizable state of a window.

## Syntax

```c
int SDL_SetWindowResizable(SDL_Window *window, SDL_bool resizable);

```

## Function Parameters

|                   |                                                                            |
| ----------------- | -------------------------------------------------------------------------- |
| **window**        | the window of which to change the resizable state                          |
| **resizable**     | [SDL_TRUE](SDL_TRUE.md) to allow resizing, [SDL_FALSE](SDL_FALSE.md) to disallow |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This will add or remove the window's
[`SDL_WINDOW_RESIZABLE`](SDL_WINDOW_RESIZABLE) flag and allow/disallow user
resizing of the window. This is a no-op if the window's resizable state
already matches the requested state.

You can't change the resizable state of a fullscreen window.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowFlags](SDL_GetWindowFlags.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
