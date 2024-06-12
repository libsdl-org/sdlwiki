###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_GetMusicPosition

Get the time current position of music stream, in seconds.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
double Mix_GetMusicPosition(Mix_Music *music);
```

## Function Parameters

|                          |           |                            |
| ------------------------ | --------- | -------------------------- |
| [Mix_Music](Mix_Music) * | **music** | the music object to query. |

## Return Value

(double) Returns -1.0 if this feature is not supported for some codec.

## Remarks

To convert to milliseconds, multiply by 1000.0.

## Version

This function is available since SDL_mixer 2.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

