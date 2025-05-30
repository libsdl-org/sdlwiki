# SDL_VideoQuit

Shut down the video subsystem, if initialized with [SDL_VideoInit](SDL_VideoInit)().

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_VideoQuit(void);
```

## Remarks

This function closes all windows, and restores the original video mode.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_VideoInit](SDL_VideoInit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

