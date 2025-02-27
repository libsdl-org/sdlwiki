# SDL_GetSystemTheme

Get the current system theme.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_SystemTheme SDL_GetSystemTheme(void);
```

## Return Value

([SDL_SystemTheme](SDL_SystemTheme)) Returns the current system theme,
light, dark, or unknown.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

