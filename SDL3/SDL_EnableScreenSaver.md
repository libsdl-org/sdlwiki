###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EnableScreenSaver

Allow the screen to be blanked by a screen saver.

## Syntax

```c
int SDL_EnableScreenSaver(void);

```

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_DisableScreenSaver](SDL_DisableScreenSaver.md)
* [SDL_ScreenSaverEnabled](SDL_ScreenSaverEnabled.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVideo](CategoryVideo.md)
