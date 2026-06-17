# SDL_HINT_ENABLE_STEAM_SCREEN_KEYBOARD

A variable that controls whether the Steam on-screen keyboard should be shown when text input is active.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_ENABLE_STEAM_SCREEN_KEYBOARD "SDL_ENABLE_STEAM_SCREEN_KEYBOARD"
```

## Remarks

Steam will set this hint via environment variable for games launched in Big
Picture mode. To override this you should call
[SDL_SetHintWithPriority](SDL_SetHintWithPriority)() with priority
[`SDL_HINT_OVERRIDE`](SDL_HINT_OVERRIDE).

The variable can be set to the following values:

- "0": Do not show the Steam on-screen keyboard.
- "1": Show the Steam on-screen keyboard.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.4.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

