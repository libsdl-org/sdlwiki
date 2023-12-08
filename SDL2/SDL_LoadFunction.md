###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LoadFunction

Look up the address of the named function in a shared object.

## Syntax

```c
void* SDL_LoadFunction(void *handle,
                       const char *name);

```

## Function Parameters

|                |                                                                             |
| -------------- | --------------------------------------------------------------------------- |
| **handle**     | a valid shared object handle returned by [SDL_LoadObject](SDL_LoadObject.md)() |
| **name**       | the name of the function to look up                                         |

## Return Value

Returns a pointer to the function or NULL if there was an error; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function pointer is no longer valid after calling
[SDL_UnloadObject](SDL_UnloadObject.md)().

This function can only look up C function names. Other languages may have
name mangling and intrinsic language support that varies from compiler to
compiler.

Make sure you declare your function pointers with the same calling
convention as the actual library function. Your code will crash
mysteriously if you do not do this.

If the requested function doesn't exist, NULL is returned.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_LoadObject](SDL_LoadObject.md)
* [SDL_UnloadObject](SDL_UnloadObject.md)

----
[CategoryAPI](CategoryAPI.md)
