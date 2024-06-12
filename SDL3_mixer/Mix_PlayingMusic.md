###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_PlayingMusic

Check the playing status of the music stream.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_PlayingMusic(void);
```

## Return Value

(int) Returns non-zero if music is playing, zero otherwise.

## Remarks

If music is currently playing, this function returns 1. Otherwise it
returns 0.

Paused music is treated as playing, even though it is not currently making
forward progress in mixing.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

