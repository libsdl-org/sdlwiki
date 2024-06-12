###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetTimidityCfg

Get full path of a previously-specified Timidity config file.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
const char* Mix_GetTimidityCfg(void);
```

## Return Value

(const char *) Returns the previously-specified path, or NULL if not set.

## Remarks

For example, "/etc/timidity.cfg"

If a path has never been specified, this returns NULL.

This returns a pointer to internal memory, and it should not be modified or
free'd by the caller.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [Mix_SetTimidityCfg](Mix_SetTimidityCfg)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

