###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_IsScreenSaverEnabled

Check whether the screensaver is currently enabled.

## Syntax

```c
SDL_bool SDL_IsScreenSaverEnabled(void);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the screensaver is enabled,
[SDL_FALSE](SDL_FALSE.md) if it is disabled.

## Remarks

The screensaver is disabled by default since SDL 2.0.2. Before SDL 2.0.2
the screensaver was enabled by default.

The default can also be changed using
[`SDL_HINT_VIDEO_ALLOW_SCREENSAVER`](SDL_HINT_VIDEO_ALLOW_SCREENSAVER).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_DisableScreenSaver](SDL_DisableScreenSaver.md)
* [SDL_EnableScreenSaver](SDL_EnableScreenSaver.md)

----
[CategoryAPI](CategoryAPI.md)
