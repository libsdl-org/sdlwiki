###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetTimidityCfg

Set full path of the Timidity config file.

## Syntax

```c
int Mix_SetTimidityCfg(const char *path);

```

## Function Parameters

|              |                                 |
| ------------ | ------------------------------- |
| **path**     | path to a Timidity config file. |

## Return Value

Returns 1 if successful, 0 on error

## Remarks

For example, "/etc/timidity.cfg"

This is obviously only useful if SDL_mixer is using Timidity internally to
play MIDI files.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
