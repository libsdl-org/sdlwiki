###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_APP_NAME

Specify an application name.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_APP_NAME "SDL_APP_NAME"
```

## Remarks

This hint lets you specify the application name sent to the OS when
required. For example, this will often appear in volume control applets for
audio streams, and in lists of applications which are inhibiting the
screensaver. You should use a string that describes your program ("My Game
2: The Revenge")

Setting this to "" or leaving it unset will have SDL use a reasonable
default: probably the application's name or "SDL Application" if SDL
doesn't have any better information.

Note that, for audio streams, this can be overridden with
[SDL_HINT_AUDIO_DEVICE_APP_NAME](SDL_HINT_AUDIO_DEVICE_APP_NAME).

On targets where this is not supported, this hint does nothing.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

