###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_SetMusicPosition

Set the current position in the music stream, in seconds.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_SetMusicPosition(double position);
```

## Function Parameters

|        |              |                                             |
| ------ | ------------ | ------------------------------------------- |
| double | **position** | the new position, in seconds (as a double). |

## Return Value

(int) Returns 0 if successful, or -1 if it failed or not implemented.

## Remarks

To convert from milliseconds, divide by 1000.0.

This function is only implemented for MOD music formats (set pattern order
number) and for WAV, OGG, FLAC, MP3, and MODPLUG music at the moment.

## Version

This function is available since SDL_mixer 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

