###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetWindowDisplayScale

Get the content display scale relative to a window's pixel size.

## Syntax

```c
float SDL_GetWindowDisplayScale(SDL_Window *window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the display scale, or 0.0f on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is a combination of the window pixel density and the display content
scale, and is the expected scale for displaying content in this window. For
example, if a 3840x2160 window had a display scale of 2.0, the user expects
the content to take twice as many pixels and be the same physical size as
if it were being displayed in a 1920x1080 window with a display scale of
1.0.

Conceptually this value corresponds to the scale display setting, and is
updated when that setting is changed, or the window moves to a display with
a different scale setting.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

