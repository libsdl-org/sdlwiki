###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_WinRTRunApp

Initialize and launch an SDL/WinRT application.

## Header File

Defined in [SDL_main.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_main.h)

## Syntax

```c
int SDL_WinRTRunApp(SDL_main_func mainFunction, void * reserved);
```

## Function Parameters

|                                |                  |                                                                  |
| ------------------------------ | ---------------- | ---------------------------------------------------------------- |
| [SDL_main_func](SDL_main_func) | **mainFunction** | the SDL app's C-style main(), an [SDL_main_func](SDL_main_func). |
| void *                         | **reserved**     | reserved for future use; should be NULL.                         |

## Return Value

(int) Returns 0 on success or -1 on failure; call
[SDL_GetError](SDL_GetError)() to retrieve more information on the failure.

## Version

This function is available since SDL 2.0.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain), [CategoryInit](CategoryInit)


