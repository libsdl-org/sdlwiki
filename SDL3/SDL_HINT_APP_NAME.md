###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_APP_NAME

Specify an application name.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

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

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

