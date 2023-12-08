###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Quit

Clean up all initialized subsystems.

## Syntax

```c
void SDL_Quit(void);

```

## Remarks

You should call this function even if you have already shutdown each
initialized subsystem with [SDL_QuitSubSystem](SDL_QuitSubSystem.md)(). It is
safe to call this function even in the case of errors in initialization.

You can use this function with atexit() to ensure that it is run when your
application is shutdown, but it is not wise to do this from a library or
other dynamically loaded code.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include "SDL.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    if (SDL_Init(SDL_INIT_EVERYTHING) != 0) {
        fprintf(stderr, "Unable to initialize SDL:  %s\n", SDL_GetError());
        return 1;
    }
    atexit(SDL_Quit);

    /* ... */

    return 0;
}
```

## Related Functions

* [SDL_Init](SDL_Init.md)
* [SDL_QuitSubSystem](SDL_QuitSubSystem.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryInit](CategoryInit.md)
