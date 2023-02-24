###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DisableScreenSaver

Prevent the screen from being blanked by a screen saver.

## Syntax

```c
int SDL_DisableScreenSaver(void);

```

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If you disable the screensaver, it is automatically re-enabled when SDL
quits.

The screensaver is disabled by default since SDL 2.0.2. Before SDL 2.0.2
the screensaver was enabled by default.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_EnableScreenSaver](SDL_EnableScreenSaver)
* [SDL_ScreenSaverEnabled](SDL_ScreenSaverEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


