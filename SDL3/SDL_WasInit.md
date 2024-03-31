###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WasInit

Get a mask of the specified subsystems which are currently initialized.

## Header File

Defined in [SDL_init.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
Uint32 SDL_WasInit(Uint32 flags);

```

## Function Parameters

|               |                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| **flags**     | any of the flags used by [SDL_Init](SDL_Init)(); see [SDL_Init](SDL_Init) for details. |

## Return Value

Returns a mask of all initialized subsystems if `flags` is 0, otherwise it
returns the initialization status of the specified subsystems.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
/* Get init data on all the subsystems */
Uint32 subsystem_init;

subsystem_init = SDL_WasInit(SDL_INIT_EVERYTHING);

if (subsystem_init & SDL_INIT_VIDEO) {
    printf("Video is initialized.\n");
} else {
    printf("Video is not initialized.\n");
}
```
```c++
/* Just check for one specific subsystem */

if (SDL_WasInit(SDL_INIT_VIDEO) != 0) {
    printf("Video is initialized.\n");
} else {
    printf("Video is not initialized.\n");
}
```
```c++
/* Check for two subsystems */
Uint32 subsystem_mask = SDL_INIT_VIDEO | SDL_INIT_AUDIO;

if (SDL_WasInit(subsystem_mask) == subsystem_mask) {
    printf("Video and Audio initialized.\n");
} else {
    printf("Video and Audio not initialized.\n");
}
```

## Related Functions

* [SDL_Init](SDL_Init)
* [SDL_InitSubSystem](SDL_InitSubSystem)

----
[CategoryAPI](CategoryAPI), [CategoryInit](CategoryInit)


