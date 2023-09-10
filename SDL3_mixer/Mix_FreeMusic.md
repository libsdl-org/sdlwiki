###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_FreeMusic

Free a music object.

## Syntax

```c
void Mix_FreeMusic(Mix_Music *music);

```

## Function Parameters

|               |                           |
| ------------- | ------------------------- |
| **music**     | the music object to free. |

## Remarks

If this music is currently playing, it will be stopped.

If this music is in the process of fading out (via
[Mix_FadeOutMusic](Mix_FadeOutMusic)()), this function will *block* until
the fade completes. If you need to avoid this, be sure to call
[Mix_HaltMusic](Mix_HaltMusic)() before freeing the music.

## Version

This function is available since SDL_mixer 3.0.0.

## Related Functions

* [Mix_LoadMUS](Mix_LoadMUS)
* [Mix_LoadMUS_RW](Mix_LoadMUS_RW)
* [Mix_LoadMUSType_RW](Mix_LoadMUSType_RW)

----
[CategoryAPI](CategoryAPI)

