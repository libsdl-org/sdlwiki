###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicLoopEndTime

Get the loop end time position of music stream, in seconds.

## Syntax

```c
double Mix_GetMusicLoopEndTime(Mix_Music *music);

```

## Function Parameters

|               |                            |
| ------------- | -------------------------- |
| **music**     | the music object to query. |

## Return Value

Returns -1.0 if this feature is not used for this music or not supported
for some codec

## Remarks

To convert to milliseconds, multiply by 1000.0.

If NULL is passed, returns duration of current playing music.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI)

