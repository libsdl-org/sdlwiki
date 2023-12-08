###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
# SDL_CaptureMouse

Capture the mouse and to track input outside an SDL window.

## Syntax

```c
int SDL_CaptureMouse(SDL_bool enabled);

```

## Function Parameters

|                 |                                                                              |
| --------------- | ---------------------------------------------------------------------------- |
| **enabled**     | [SDL_TRUE](SDL_TRUE.md) to enable capturing, [SDL_FALSE](SDL_FALSE.md) to disable. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Capturing enables your app to obtain mouse events globally, instead of just
within your window. Not all video targets support this function. When
capturing is enabled, the current window will get all mouse events, but
unlike relative mode, no change is made to the cursor and it is not
restrained to your window.

This function may also deny mouse input to other windows--both those in
your application and others on the system--so you should use this function
sparingly, and in small bursts. For example, you might want to track the
mouse while the user is dragging something, until the user releases a mouse
button. It is not recommended that you capture the mouse for long periods
of time, such as the entire time your app is running. For that, you should
probably use [SDL_SetRelativeMouseMode](SDL_SetRelativeMouseMode.md)() or
[SDL_SetWindowGrab](SDL_SetWindowGrab.md)(), depending on your goals.

While captured, mouse events still report coordinates relative to the
current (foreground) window, but those coordinates may be outside the
bounds of the window (including negative values). Capturing is only allowed
for the foreground window. If the window loses focus while capturing, the
capture will be disabled automatically.

While capturing is enabled, the current window will have the
[`SDL_WINDOW_MOUSE_CAPTURE`](SDL_WINDOW_MOUSE_CAPTURE) flag set.

Please note that as of SDL 2.0.22, SDL will attempt to "auto capture" the
mouse while the user is pressing a button; this is to try and make mouse
behavior more consistent between platforms, and deal with the common case
of a user dragging the mouse outside of the window. This means that if you
are calling [SDL_CaptureMouse](SDL_CaptureMouse.md)() only to deal with this
situation, you no longer have to (although it is safe to do so). If this
causes problems for your app, you can disable auto capture by setting the
[`SDL_HINT_MOUSE_AUTO_CAPTURE`](SDL_HINT_MOUSE_AUTO_CAPTURE) hint to zero.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryMouse](CategoryMouse.md), [CategoryDraft](CategoryDraft.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
