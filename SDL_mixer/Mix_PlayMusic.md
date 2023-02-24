###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_PlayMusic

Play a new music object.

## Syntax

```c
int Mix_PlayMusic(Mix_Music *music, int loops);

```

## Function Parameters

|               |                                                                           |
| ------------- | ------------------------------------------------------------------------- |
| **music**     | the new music object to schedule for mixing.                              |
| **loops**     | the number of loops to play the music for (0 means "play once and stop"). |

## Return Value

Returns zero on success, -1 on error.

## Remarks

This will schedule the music object to begin mixing for playback.

There is only ever one music object playing at a time; if this is called
when another music object is playing, the currently-playing music is halted
and the new music will replace it.

Please note that if the currently-playing music is in the process of fading
out (via [Mix_FadeOutMusic](Mix_FadeOutMusic)()), this function will
*block* until the fade completes. If you need to avoid this, be sure to
call [Mix_HaltMusic](Mix_HaltMusic)() before starting new music.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI)

