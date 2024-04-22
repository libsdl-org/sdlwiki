###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINDOWS_FORCE_MUTEX_CRITICAL_SECTIONS

Force SDL to use Critical Sections for mutexes on Windows.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_FORCE_MUTEX_CRITICAL_SECTIONS "SDL_WINDOWS_FORCE_MUTEX_CRITICAL_SECTIONS"
```

## Remarks

On Windows 7 and newer, Slim Reader/Writer Locks are available. They offer
better performance, allocate no kernel ressources and use less memory. SDL
will fall back to Critical Sections on older OS versions or if forced to by
this hint.

This variable can be set to the following values: "0" - Use SRW Locks when
available. If not, fall back to Critical Sections. (default) "1" - Force
the use of Critical Sections in all cases.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

