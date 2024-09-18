###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetTimidityCfg

Set full path of the Timidity config file.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_SetTimidityCfg(const char *path);
```

## Function Parameters

|              |          |                                 |
| ------------ | -------- | ------------------------------- |
| const char * | **path** | path to a Timidity config file. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

For example, "/etc/timidity.cfg"

This is obviously only useful if SDL_mixer is using Timidity internally to
play MIDI files.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

