# SDL_GDKRunApp

Initialize and launch an SDL GDK application.

## Header File

Defined in [SDL_main.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_main.h)

## Syntax

```c
int SDL_GDKRunApp(SDL_main_func mainFunction, void *reserved);
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

This function is available since SDL 2.24.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMain](CategoryMain)

