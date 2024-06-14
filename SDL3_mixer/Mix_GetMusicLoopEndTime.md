###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicLoopEndTime

Get the loop end time position of music stream, in seconds.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
double Mix_GetMusicLoopEndTime(Mix_Music *music);
```

## Function Parameters

|                          |           |                            |
| ------------------------ | --------- | -------------------------- |
| [Mix_Music](Mix_Music) * | **music** | the music object to query. |

## Return Value

(double) Returns -1.0 if this feature is not used for this music or not
supported for some codec.

## Remarks

To convert to milliseconds, multiply by 1000.0.

If NULL is passed, returns duration of current playing music.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

