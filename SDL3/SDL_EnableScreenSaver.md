###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EnableScreenSaver

Allow the screen to be blanked by a screen saver.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_bool SDL_EnableScreenSaver(void);
```

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_DisableScreenSaver](SDL_DisableScreenSaver)
- [SDL_ScreenSaverEnabled](SDL_ScreenSaverEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

