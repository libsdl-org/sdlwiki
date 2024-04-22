###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsScreenSaverEnabled

Check whether the screensaver is currently enabled.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
SDL_bool SDL_IsScreenSaverEnabled(void);

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

This function is available since SDL 2.0.0.

## See Also

* [SDL_DisableScreenSaver](SDL_DisableScreenSaver)
* [SDL_EnableScreenSaver](SDL_EnableScreenSaver)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

