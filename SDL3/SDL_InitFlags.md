###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_InitFlags

Initialization flags for [SDL_Init](SDL_Init) and/or [SDL_InitSubSystem](SDL_InitSubSystem)

## Header File

Defined in [SDL_init.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef enum SDL_InitFlags
{
    SDL_INIT_TIMER        = 0x00000001,
    SDL_INIT_AUDIO        = 0x00000010,  /**< `SDL_INIT_AUDIO` implies `SDL_INIT_EVENTS` */
    SDL_INIT_VIDEO        = 0x00000020,  /**< `SDL_INIT_VIDEO` implies `SDL_INIT_EVENTS` */
    SDL_INIT_JOYSTICK     = 0x00000200,  /**< `SDL_INIT_JOYSTICK` implies `SDL_INIT_EVENTS` */
    SDL_INIT_HAPTIC       = 0x00001000,
    SDL_INIT_GAMEPAD      = 0x00002000,  /**< `SDL_INIT_GAMEPAD` implies `SDL_INIT_JOYSTICK` */
    SDL_INIT_EVENTS       = 0x00004000,
    SDL_INIT_SENSOR       = 0x00008000,  /**< `SDL_INIT_SENSOR` implies `SDL_INIT_EVENTS` */
    SDL_INIT_CAMERA       = 0x00010000   /**< `SDL_INIT_CAMERA` implies `SDL_INIT_EVENTS` */
} SDL_InitFlags;
```

## Remarks

These are the flags which may be passed to [SDL_Init](SDL_Init)(). You
should specify the subsystems which you will be using in your application.

## See Also

* [SDL_Init](SDL_Init)
* [SDL_Quit](SDL_Quit)
* [SDL_InitSubSystem](SDL_InitSubSystem)
* [SDL_QuitSubSystem](SDL_QuitSubSystem)
* [SDL_WasInit](SDL_WasInit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

