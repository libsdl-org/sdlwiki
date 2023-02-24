###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UIKitRunApp

Initializes and launches an SDL application.

## Syntax

```c
int SDL_UIKitRunApp(int argc, char *argv[], SDL_main_func mainFunction);

```

## Function Parameters

|                      |                                                                 |
| -------------------- | --------------------------------------------------------------- |
| **argc**             | The argc parameter from the application's main() function       |
| **argv**             | The argv parameter from the application's main() function       |
| **mainFunction**     | The SDL app's C-style main(), an [SDL_main_func](SDL_main_func) |

## Return Value

Return the return value from mainFunction

## Version

This function is available since SDL 2.0.10.

----
[CategoryAPI](CategoryAPI)

