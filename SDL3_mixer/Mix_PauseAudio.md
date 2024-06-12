###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_PauseAudio

Suspend or resume the whole audio output.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void Mix_PauseAudio(int pause_on);
```

## Function Parameters

|     |              |                                          |
| --- | ------------ | ---------------------------------------- |
| int | **pause_on** | 1 to pause audio output, or 0 to resume. |

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

