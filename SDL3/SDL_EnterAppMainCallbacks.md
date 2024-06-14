###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_EnterAppMainCallbacks

An entry point for SDL's use in [SDL_MAIN_USE_CALLBACKS](SDL_MAIN_USE_CALLBACKS).

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
int SDL_EnterAppMainCallbacks(int argc, char* argv[], SDL_AppInit_func appinit, SDL_AppIterate_func appiter, SDL_AppEvent_func appevent, SDL_AppQuit_func appquit);
```

## Function Parameters

|                                            |              |                                                              |
| ------------------------------------------ | ------------ | ------------------------------------------------------------ |
| int                                        | **argc**     | standard Unix main argc.                                     |
| char **                                    | **argv**     | standard Unix main argv.                                     |
| [SDL_AppInit_func](SDL_AppInit_func)       | **appinit**  | the application's [SDL_AppInit](SDL_AppInit) function.       |
| [SDL_AppIterate_func](SDL_AppIterate_func) | **appiter**  | the application's [SDL_AppIterate](SDL_AppIterate) function. |
| [SDL_AppEvent_func](SDL_AppEvent_func)     | **appevent** | the application's [SDL_AppEvent](SDL_AppEvent) function.     |
| [SDL_AppQuit_func](SDL_AppQuit_func)       | **appquit**  | the application's [SDL_AppQuit](SDL_AppQuit) function.       |

## Return Value

(int) Returns standard Unix main return value.

## Remarks

Generally, you should not call this function directly. This only exists to
hand off work into SDL as soon as possible, where it has a lot more control
and functionality available, and make the inline code in
[SDL_main](SDL_main).h as small as possible.

Not all platforms use this, it's actual use is hidden in a magic
header-only library, and you should not call this directly unless you
_really_ know what you're doing.

## Thread Safety

It is not safe to call this anywhere except as the only function call in
[SDL_main](SDL_main).

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

