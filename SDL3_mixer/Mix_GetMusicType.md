###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicType

Find out the format of a mixer music.

## Syntax

```c
Mix_MusicType Mix_GetMusicType(const Mix_Music *music);

```

## Function Parameters

|               |                                                                     |
| ------------- | ------------------------------------------------------------------- |
| **music**     | the music object to query, or NULL for the currently-playing music. |

## Return Value

Returns the [Mix_MusicType](Mix_MusicType) for the music object.

## Remarks

If `music` is NULL, this will query the currently playing music (and return
MUS_NONE if nothing is currently playing).

## Version

This function is available since SDL_mixer 3.0.0

----
[CategoryAPI](CategoryAPI)

