###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GDKRunApp

Initialize and launch an SDL GDK application.

## Header File

Defined in [SDL_main.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_main.h)

## Syntax

```c
int SDL_GDKRunApp(SDL_main_func mainFunction, void *reserved);

```

## Function Parameters

|                      |                                                                 |
| -------------------- | --------------------------------------------------------------- |
| **mainFunction**     | the SDL app's C-style main(), an [SDL_main_func](SDL_main_func) |
| **reserved**         | reserved for future use; should be NULL                         |

## Return Value

Returns 0 on success or -1 on failure; call [SDL_GetError](SDL_GetError)()
to retrieve more information on the failure.

## Version

This function is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

