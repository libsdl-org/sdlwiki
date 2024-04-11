###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_main_func

The prototype for the application's main() function

## Header File

Defined in [SDL_main.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef int (SDLCALL *SDL_main_func)(int argc, char *argv[]);
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

