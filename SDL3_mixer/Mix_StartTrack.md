###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_StartTrack

Start a track in music object.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_StartTrack(Mix_Music *music, int track);
```

## Function Parameters

|                          |           |                                                 |
| ------------------------ | --------- | ----------------------------------------------- |
| [Mix_Music](Mix_Music) * | **music** | the music object.                               |
| int                      | **track** | the track number to play. 0 is the first track. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This only applies to GME music formats.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

