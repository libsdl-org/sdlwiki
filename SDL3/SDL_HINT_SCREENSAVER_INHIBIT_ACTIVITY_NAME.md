# SDL_HINT_SCREENSAVER_INHIBIT_ACTIVITY_NAME

Specify an "activity name" for screensaver inhibition.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_SCREENSAVER_INHIBIT_ACTIVITY_NAME "SDL_SCREENSAVER_INHIBIT_ACTIVITY_NAME"
```

## Remarks

Some platforms, notably Linux desktops, list the applications which are
inhibiting the screensaver or other power-saving features.

This hint lets you specify the "activity name" sent to the OS when
[SDL_DisableScreenSaver](SDL_DisableScreenSaver)() is used (or the
screensaver is automatically disabled). The contents of this hint are used
when the screensaver is disabled. You should use a string that describes
what your program is doing (and, therefore, why the screensaver is
disabled). For example, "Playing a game" or "Watching a video".

Setting this to "" or leaving it unset will have SDL use a reasonable
default: "Playing a game" or something similar.

This hint should be set before calling
[SDL_DisableScreenSaver](SDL_DisableScreenSaver)()

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

