# SDL_CaptureMouse

Capture the mouse and to track input outside an SDL window.

## Header File

Defined in [<SDL3/SDL_mouse.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mouse.h)

## Syntax

```c
bool SDL_CaptureMouse(bool enabled);
```

## Function Parameters

|      |             |                                             |
| ---- | ----------- | ------------------------------------------- |
| bool | **enabled** | true to enable capturing, false to disable. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

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
probably use
[SDL_SetWindowRelativeMouseMode](SDL_SetWindowRelativeMouseMode)() or
[SDL_SetWindowMouseGrab](SDL_SetWindowMouseGrab)(), depending on your
goals.

While captured, mouse events still report coordinates relative to the
current (foreground) window, but those coordinates may be outside the
bounds of the window (including negative values). Capturing is only allowed
for the foreground window. If the window loses focus while capturing, the
capture will be disabled automatically.

While capturing is enabled, the current window will have the
[`SDL_WINDOW_MOUSE_CAPTURE`](SDL_WINDOW_MOUSE_CAPTURE) flag set.

Please note that SDL will attempt to "auto capture" the mouse while the
user is pressing a button; this is to try and make mouse behavior more
consistent between platforms, and deal with the common case of a user
dragging the mouse outside of the window. This means that if you are
calling [SDL_CaptureMouse](SDL_CaptureMouse)() only to deal with this
situation, you do not have to (although it is safe to do so). If this
causes problems for your app, you can disable auto capture by setting the
[`SDL_HINT_MOUSE_AUTO_CAPTURE`](SDL_HINT_MOUSE_AUTO_CAPTURE) hint to zero.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetGlobalMouseState](SDL_GetGlobalMouseState)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMouse](CategoryMouse)

