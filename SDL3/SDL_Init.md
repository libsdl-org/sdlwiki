###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Init

Initialize the SDL library.

## Header File

Defined in [SDL_init.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_Init(Uint32 flags);

```

## Function Parameters

|               |                                |
| ------------- | ------------------------------ |
| **flags**     | subsystem initialization flags |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

[SDL_Init](SDL_Init)() simply forwards to calling
[SDL_InitSubSystem](SDL_InitSubSystem)(). Therefore, the two may be used
interchangeably. Though for readability of your code
[SDL_InitSubSystem](SDL_InitSubSystem)() might be preferred.

The file I/O (for example: [SDL_IOFromFile](SDL_IOFromFile)) and threading
([SDL_CreateThread](SDL_CreateThread)) subsystems are initialized by
default. Message boxes
([SDL_ShowSimpleMessageBox](SDL_ShowSimpleMessageBox)) also attempt to work
without initializing the video subsystem, in hopes of being useful in
showing an error dialog when [SDL_Init](SDL_Init) fails. You must
specifically initialize other subsystems if you use them in your
application.

Logging (such as [SDL_Log](SDL_Log)) works without initialization, too.

`flags` may be any of the following OR'd together:

- [`SDL_INIT_TIMER`](SDL_INIT_TIMER): timer subsystem
- [`SDL_INIT_AUDIO`](SDL_INIT_AUDIO): audio subsystem
- [`SDL_INIT_VIDEO`](SDL_INIT_VIDEO): video subsystem; automatically
  initializes the events subsystem
- [`SDL_INIT_JOYSTICK`](SDL_INIT_JOYSTICK): joystick subsystem;
  automatically initializes the events subsystem
- [`SDL_INIT_HAPTIC`](SDL_INIT_HAPTIC): haptic (force feedback) subsystem
- [`SDL_INIT_GAMEPAD`](SDL_INIT_GAMEPAD): gamepad subsystem; automatically
  initializes the joystick subsystem
- [`SDL_INIT_EVENTS`](SDL_INIT_EVENTS): events subsystem
- [`SDL_INIT_SENSOR`](SDL_INIT_SENSOR): sensor subsystem

Subsystem initialization is ref-counted, you must call
[SDL_QuitSubSystem](SDL_QuitSubSystem)() for each
[SDL_InitSubSystem](SDL_InitSubSystem)() to correctly shutdown a subsystem
manually (or call [SDL_Quit](SDL_Quit)() to force shutdown). If a subsystem
is already loaded then this call will increase the ref-count and return.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
#include "SDL.h"

int main(int argc, char* argv[])
{
    if (SDL_Init(SDL_INIT_VIDEO|SDL_INIT_AUDIO) != 0) {
        SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
        return 1;
    }

    /* ... */

    SDL_Quit();

    return 0;
}
```

## See Also

* [SDL_InitSubSystem](SDL_InitSubSystem)
* [SDL_Quit](SDL_Quit)
* [SDL_SetMainReady](SDL_SetMainReady)
* [SDL_WasInit](SDL_WasInit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)


