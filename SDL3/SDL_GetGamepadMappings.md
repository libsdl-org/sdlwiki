###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetGamepadMappings

Get the mapping at a particular index.

## Syntax

```c
char ** SDL_GetGamepadMappings(int *count);

```

## Function Parameters

|               |                                                                        |
| ------------- | ---------------------------------------------------------------------- |
| **count**     | a pointer filled in with the number of mappings returned, can be NULL. |

## Return Value

Returns an array of the mapping strings, NULL-terminated. Must be freed
with [SDL_free](SDL_free)(). Returns NULL on error.

## Remarks

You must free the returned pointer with [SDL_free](SDL_free)() when you are
done with it, but you do _not_ free each string in the array.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

