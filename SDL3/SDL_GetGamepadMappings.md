# SDL_GetGamepadMappings

Get the current gamepad mappings.

## Header File

Defined in [<SDL3/SDL_gamepad.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gamepad.h)

## Syntax

```c
char ** SDL_GetGamepadMappings(int *count);
```

## Function Parameters

|       |           |                                                                        |
| ----- | --------- | ---------------------------------------------------------------------- |
| int * | **count** | a pointer filled in with the number of mappings returned, can be NULL. |

## Return Value

(char **) Returns an array of the mapping strings, NULL-terminated, or NULL
on failure; call [SDL_GetError](SDL_GetError)() for more information. This
is a single allocation that should be freed with [SDL_free](SDL_free)()
when it is no longer needed.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGamepad](CategoryGamepad)

