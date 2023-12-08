###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicVolume

Query the current volume value for a music object.

## Syntax

```c
int Mix_GetMusicVolume(Mix_Music *music);

```

## Function Parameters

|               |                            |
| ------------- | -------------------------- |
| **music**     | the music object to query. |

## Return Value

Returns the music's current volume, between 0 and
[MIX_MAX_VOLUME](MIX_MAX_VOLUME.md) (128).

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI.md)
