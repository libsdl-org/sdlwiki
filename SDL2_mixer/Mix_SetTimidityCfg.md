###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetTimidityCfg

Set full path of the Timidity config file.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_SetTimidityCfg(const char *path);
```

## Function Parameters

|              |          |                                 |
| ------------ | -------- | ------------------------------- |
| const char * | **path** | path to a Timidity config file. |

## Return Value

(int) Returns 1 if successful, 0 on error.

## Remarks

For example, "/etc/timidity.cfg"

This is obviously only useful if SDL_mixer is using Timidity internally to
play MIDI files.

## Version

This function is available since SDL_mixer 2.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

