###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_QTWAYLAND_CONTENT_ORIENTATION

A variable describing the content orientation on QtWayland-based platforms.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_QTWAYLAND_CONTENT_ORIENTATION "SDL_QTWAYLAND_CONTENT_ORIENTATION"
```

## Remarks

On QtWayland platforms, windows are rotated client-side to allow for custom
transitions. In order to correctly position overlays (e.g. volume bar) and
gestures (e.g. events view, close/minimize gestures), the system needs to
know in which orientation the application is currently drawing its
contents.

This does not cause the window to be rotated or resized, the application
needs to take care of drawing the content in the right orientation (the
framebuffer is always in portrait mode).

This variable can be one of the following values:

- "primary" (default)
- "portrait"
- "landscape"
- "inverted-portrait"
- "inverted-landscape"

Since SDL 2.0.22 this variable accepts a comma-separated list of values
above.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

