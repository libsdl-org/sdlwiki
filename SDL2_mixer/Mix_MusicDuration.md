###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_MusicDuration

Get a music object's duration, in seconds.

## Syntax

```c
double Mix_MusicDuration(Mix_Music *music);

```

## Function Parameters

|               |                            |
| ------------- | -------------------------- |
| **music**     | the music object to query. |

## Return Value

Returns music duration in seconds, or -1.0 on error.

## Remarks

To convert to milliseconds, multiply by 1000.0.

If NULL is passed, returns duration of current playing music.

## Version

This function is available since SDL_mixer 2.6.0.

----
[CategoryAPI](CategoryAPI.md)
