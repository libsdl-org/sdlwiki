###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ScreenSaverEnabled

Check whether the screensaver is currently enabled.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
bool SDL_ScreenSaverEnabled(void);
```

## Return Value

(bool) Returns true if the screensaver is enabled, false if it is disabled.

## Remarks

The screensaver is disabled by default.

The default can also be changed using
[`SDL_HINT_VIDEO_ALLOW_SCREENSAVER`](SDL_HINT_VIDEO_ALLOW_SCREENSAVER).

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_DisableScreenSaver](SDL_DisableScreenSaver)
- [SDL_EnableScreenSaver](SDL_EnableScreenSaver)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

