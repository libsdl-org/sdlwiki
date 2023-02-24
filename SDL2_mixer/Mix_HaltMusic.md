###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_HaltMusic

Halt playing of the music stream.

## Syntax

```c
int Mix_HaltMusic(void);

```

## Return Value

Returns zero, regardless of whether any music was halted.

## Remarks

This will stop further playback of music until a new music object is
started there.

Any halted music will call any callback specified by
[Mix_HookMusicFinished](Mix_HookMusicFinished)() before this function
returns.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

