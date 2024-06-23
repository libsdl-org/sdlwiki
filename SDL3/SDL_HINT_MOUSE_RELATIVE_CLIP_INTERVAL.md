###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MOUSE_RELATIVE_CLIP_INTERVAL

Controls how often SDL issues cursor confinement commands to the operating system while relative mode is active, in case the desired confinement state became out-of-sync due to interference from other running programs.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_CLIP_INTERVAL  "SDL_MOUSE_RELATIVE_CLIP_INTERVAL"
```

## Remarks

The variable can be integers representing miliseconds between each refresh.
A value of zero means SDL will not automatically refresh the confinement.
The default value varies depending on the operating system, this variable
might not have any effects on inapplicable platforms such as those without
a cursor.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

