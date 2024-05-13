###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_AUDIO_DEVICE_APP_ICON_NAME

Specify an application icon name for an audio device.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DEVICE_APP_ICON_NAME "SDL_AUDIO_DEVICE_APP_ICON_NAME"
```

## Remarks

Some audio backends (such as Pulseaudio and Pipewire) allow you to set an
XDG icon name for your application. Among other things, this icon might
show up in a system control panel that lets the user adjust the volume on
specific audio streams instead of using one giant master volume slider.
Note that this is unrelated to the icon used by the windowing system, which
may be set with [SDL_SetWindowIcon](SDL_SetWindowIcon) (or via desktop file
on Wayland).

Setting this to "" or leaving it unset will have SDL use a reasonable
default, "applications-games", which is likely to be installed. See
https://specifications.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html
and
https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html
for the relevant XDG icon specs.

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

