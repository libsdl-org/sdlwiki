###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_QUIT_ON_LAST_WINDOW_CLOSE

A variable that decides whether to send [SDL_QUIT](SDL_QUIT) when closing the final window.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_QUIT_ON_LAST_WINDOW_CLOSE "SDL_QUIT_ON_LAST_WINDOW_CLOSE"
```

## Remarks

By default, SDL sends an [SDL_QUIT](SDL_QUIT) event when there is only one
window and it receives an [SDL_WINDOWEVENT_CLOSE](SDL_WINDOWEVENT_CLOSE)
event, under the assumption most apps would also take the loss of this
window as a signal to terminate the program.

However, it's not unreasonable in some cases to have the program continue
to live on, perhaps to create new windows later.

Changing this hint to "0" will cause SDL to not send an
[SDL_QUIT](SDL_QUIT) event when the final window is requesting to close.
Note that in this case, there are still other legitimate reasons one might
get an [SDL_QUIT](SDL_QUIT) event: choosing "Quit" from the macOS menu bar,
sending a SIGINT (ctrl-c) on Unix, etc.

The default value is "1". This hint can be changed at any time.

This hint is available since SDL 2.0.22. Before then, you always get an
[SDL_QUIT](SDL_QUIT) event when closing the final window.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

