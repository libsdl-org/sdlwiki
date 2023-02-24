###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RunApp

Initializes and launches an SDL application, by doing platform-specific initialization before calling your mainFunction and cleanups after it returns, if that is needed for a specific platform, otherwise it just calls mainFunction.

## Syntax

```c
int SDL_RunApp(int argc, char* argv[], SDL_main_func mainFunction, void * reserved);

```

## Function Parameters

|                      |                                                                                                                                                                                                          |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **argc**             | The argc parameter from the application's main() function, or 0 if the platform's main-equivalent has no argc                                                                                            |
| **argv**             | The argv parameter from the application's main() function, or NULL if the platform's main-equivalent has no argv                                                                                         |
| **mainFunction**     | Your SDL app's C-style main(), an [SDL_main_func](SDL_main_func). NOT the function you're calling this from! Its name doesn't matter, but its signature must be like int my_main(int argc, char* argv[]) |
| **reserved**         | should be NULL (reserved for future use, will probably be platform-specific then)                                                                                                                        |

## Return Value

Returns the return value from mainFunction: 0 on success, -1 on failure;
[SDL_GetError](SDL_GetError)() might have more information on the failure

## Remarks

You can use this if you want to use your own main() implementation without
using [SDL_main](SDL_main) (like when using
[SDL_MAIN_HANDLED](SDL_MAIN_HANDLED)). When using this, you do *not* need
[SDL_SetMainReady](SDL_SetMainReady)().

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

