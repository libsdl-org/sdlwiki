###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_PlayingMusic

Check the playing status of the music stream.

## Syntax

```c
int Mix_PlayingMusic(void);

```

## Return Value

Returns non-zero if music is playing, zero otherwise.

## Remarks

If music is currently playing, this function returns 1. Otherwise it
returns 0.

Paused music is treated as playing, even though it is not currently making
forward progress in mixing.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
