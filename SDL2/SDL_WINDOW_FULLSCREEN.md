# SDL_WINDOW_FULLSCREEN

Flag to request a fullscreen window, possibly with a resolution change.

# Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Remarks

If this window flag is included in [SDL_CreateWindow](SDL_CreateWindow)'s
flags, the window will be created in fullscreen mode.

SDL may change the display's resolution to accomodate this window. If you
just want to cover the entire screen, and your game can deal with arbitrary
resolutions, you should use `SDL_WINDOW_FULLSCREEN_DESKTOP` instead of this
flag, as it will _not_ change the display's resolution.

## See Also

- [SDL_WindowFlags](SDL_WindowFlags)

