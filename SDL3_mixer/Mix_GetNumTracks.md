###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetNumTracks

Get number of tracks in music object.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int Mix_GetNumTracks(Mix_Music *music);
```

## Function Parameters

|                          |           |                   |
| ------------------------ | --------- | ----------------- |
| [Mix_Music](Mix_Music) * | **music** | the music object. |

## Return Value

(int) Returns number of tracks if successful, or -1 if failed or isn't
implemented.

## Remarks

This only applies to GME music formats.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

