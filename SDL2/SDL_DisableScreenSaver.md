###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DisableScreenSaver

Prevent the screen from being blanked by a screen saver.

## Syntax

```c
void SDL_DisableScreenSaver(void);

```

## Remarks

If you disable the screensaver, it is automatically re-enabled when SDL
quits.

The screensaver is disabled by default since SDL 2.0.2. Before SDL 2.0.2
the screensaver was enabled by default.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_EnableScreenSaver](SDL_EnableScreenSaver)
* [SDL_IsScreenSaverEnabled](SDL_IsScreenSaverEnabled)

----
[CategoryAPI](CategoryAPI)

