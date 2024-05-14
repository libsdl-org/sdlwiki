###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINDOWS_FORCE_MUTEX_CRITICAL_SECTIONS

A variable controlling whether SDL uses Critical Sections for mutexes on Windows.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_FORCE_MUTEX_CRITICAL_SECTIONS "SDL_WINDOWS_FORCE_MUTEX_CRITICAL_SECTIONS"
```

## Remarks

On Windows 7 and newer, Slim Reader/Writer Locks are available. They offer
better performance, allocate no kernel resources and use less memory. SDL
will fall back to Critical Sections on older OS versions or if forced to by
this hint.

The variable can be set to the following values:

- "0": Use SRW Locks when available, otherwise fall back to Critical
  Sections. (default)
- "1": Force the use of Critical Sections in all cases.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

