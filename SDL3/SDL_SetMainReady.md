###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetMainReady

Circumvent failure of [SDL_Init](SDL_Init)() when not using [SDL_main](SDL_main)() as an entry point.

## Header File

Defined in [SDL_main.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
void SDL_SetMainReady(void);

```

## Remarks

This function is defined in [SDL_main](SDL_main).h, along with the
preprocessor rule to redefine main() as [SDL_main](SDL_main)(). Thus to
ensure that your main() function will not be changed it is necessary to
define [SDL_MAIN_HANDLED](SDL_MAIN_HANDLED) before including SDL.h.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
#define SDL_MAIN_HANDLED
#include <SDL3/SDL.h>
#include <SDL3/SDL_main.h>

int main(int argc, char *argv[])
{
    SDL_SetMainReady();
    SDL_Init(SDL_INIT_VIDEO);

    /* ... */

    SDL_Quit();

    return 0;
}
```

## See Also

* [SDL_Init](SDL_Init)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)


