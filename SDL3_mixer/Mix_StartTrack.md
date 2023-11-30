###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_StartTrack

Start a track in music object.

## Syntax

```c
int Mix_StartTrack(Mix_Music *music, int track);

```

## Function Parameters

|               |                                                 |
| ------------- | ----------------------------------------------- |
| **music**     | the music object.                               |
| **track**     | the track number to play. 0 is the first track. |

## Return Value

Returns 0 if successful, or -1 if failed or isn't implemented.

## Remarks

This only applies to GME music formats.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI)

