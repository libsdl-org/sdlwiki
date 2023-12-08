###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_SetWindowModalFor

Set the window as a modal for another window.

## Syntax

```c
int SDL_SetWindowModalFor(SDL_Window *modal_window, SDL_Window *parent_window);

```

## Function Parameters

|                       |                                        |
| --------------------- | -------------------------------------- |
| **modal_window**      | the window that should be set modal    |
| **parent_window**     | the parent window for the modal window |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
