###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_InitSubSystem

Compatibility function to initialize the SDL library.

## Header File

Defined in [SDL_init.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_InitSubSystem(Uint32 flags);

```

## Function Parameters

|               |                                                                                        |
| ------------- | -------------------------------------------------------------------------------------- |
| **flags**     | any of the flags used by [SDL_Init](SDL_Init)(); see [SDL_Init](SDL_Init) for details. |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function and [SDL_Init](SDL_Init)() are interchangeable.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
/* Separating Joystick and Video initialization. */
SDL_Init(SDL_INIT_VIDEO);

SDL_Window* window = SDL_CreateWindow("A Window",
    SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480,
    SDL_WINDOW_FULLSCREEN);
SDL_Renderer* renderer = SDL_CreateRenderer(window, NULL, 0);

/* Do Some Video stuff */

/* Initialize the joystick subsystem */
SDL_InitSubSystem(SDL_INIT_JOYSTICK);

/* Do some stuff with video and joystick */

/* Shut them both down */
SDL_Quit();
```

## Related Functions

* [SDL_Init](SDL_Init)
* [SDL_Quit](SDL_Quit)
* [SDL_QuitSubSystem](SDL_QuitSubSystem)

----
[CategoryAPI](CategoryAPI), [CategoryInit](CategoryInit)


