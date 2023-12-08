###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AudioInit

Use this function to initialize a particular audio driver.

## Syntax

```c
int SDL_AudioInit(const char *driver_name);

```

## Function Parameters

|                     |                                      |
| ------------------- | ------------------------------------ |
| **driver_name**     | the name of the desired audio driver |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This function is used internally, and should not be used unless you have a
specific need to designate the audio driver you want to use. You should
normally use [SDL_Init](SDL_Init.md)() or
[SDL_InitSubSystem](SDL_InitSubSystem.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AudioQuit](SDL_AudioQuit.md)

----
[CategoryAPI](CategoryAPI.md)
