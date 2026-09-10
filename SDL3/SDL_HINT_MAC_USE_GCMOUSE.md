# SDL_HINT_MAC_USE_GCMOUSE

A variable controlling whether the GCMouse API will be used on macOS.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MAC_USE_GCMOUSE "SDL_MAC_USE_GCMOUSE"
```

## Remarks

On supported versions of macOS, GCMouse is usually a better way to read
mouse input, but may cause problems in some scenarios (remote control
software that wants to send non-GCMouse input events, etc).

When GCMouse is disabled, SDL will use standard Cocoa mouse events.

The variable can be set to the following values:

- "0": GCMouse won't be used.
- "1": GCMouse will be used if available. (default)

This hint needs to be set before [SDL_Init](SDL_Init)().

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

