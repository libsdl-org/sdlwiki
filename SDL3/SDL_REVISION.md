###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_REVISION

This macro is a string describing the source at a particular point in development.

## Header File

Defined in [SDL_revision.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_revision.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_REVISION "Some arbitrary string decided at SDL build time"
```

## Remarks

This string is often generated from revision control's state at build time.

This string can be quite complex and does not follow any standard. For
example, it might be something like "SDL-prerelease-3.1.1-47-gf687e0732".
It might also be user-defined at build time, so it's best to treat it as a
clue in debugging forensics and not something the app will parse in any
way.

## Version

This macro is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

