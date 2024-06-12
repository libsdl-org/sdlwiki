###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicType

Find out the format of a mixer music.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
Mix_MusicType Mix_GetMusicType(const Mix_Music *music);
```

## Function Parameters

|                                |           |                                                                     |
| ------------------------------ | --------- | ------------------------------------------------------------------- |
| const [Mix_Music](Mix_Music) * | **music** | the music object to query, or NULL for the currently-playing music. |

## Return Value

([Mix_MusicType](Mix_MusicType)) Returns the [Mix_MusicType](Mix_MusicType)
for the music object.

## Remarks

If `music` is NULL, this will query the currently playing music (and return
MUS_NONE if nothing is currently playing).

## Version

This function is available since SDL_mixer 3.0.0

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

