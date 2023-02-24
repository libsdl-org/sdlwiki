###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ScreenSaverEnabled

Check whether the screensaver is currently enabled.

## Syntax

```c
SDL_bool SDL_ScreenSaverEnabled(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the screensaver is enabled,
[SDL_FALSE](SDL_FALSE) if it is disabled.

## Remarks

The screensaver is disabled by default since SDL 2.0.2. Before SDL 2.0.2
the screensaver was enabled by default.

The default can also be changed using
[`SDL_HINT_VIDEO_ALLOW_SCREENSAVER`](SDL_HINT_VIDEO_ALLOW_SCREENSAVER).

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_DisableScreenSaver](SDL_DisableScreenSaver)
* [SDL_EnableScreenSaver](SDL_EnableScreenSaver)

----
[CategoryAPI](CategoryAPI)

