###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_DestroyEnvironment

Destroy a set of environment variables.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_DestroyEnvironment(SDL_Environment *env);
```

## Function Parameters

|                                      |         |                             |
| ------------------------------------ | ------- | --------------------------- |
| [SDL_Environment](SDL_Environment) * | **env** | the environment to destroy. |

## Thread Safety

It is safe to call this function from any thread, as long as the
environment is no longer in use.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateEnvironment](SDL_CreateEnvironment)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

