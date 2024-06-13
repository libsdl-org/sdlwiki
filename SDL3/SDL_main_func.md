###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_main_func

The prototype for the application's main() function

## Header File

Defined in [<SDL3/SDL_main.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_main.h)

## Syntax

```c
typedef int (SDLCALL *SDL_main_func)(int argc, char *argv[]);
```

## Function Parameters

|          |                                       |
| -------- | ------------------------------------- |
| **argc** | an ANSI-C style main function's argc. |
| **argv** | an ANSI-C style main function's argv. |

## Return Value

Returns an ANSI-C main return code; generally 0 is considered successful
program completion, and small non-zero values are considered errors.

## Version

This datatype is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryMain](CategoryMain)

