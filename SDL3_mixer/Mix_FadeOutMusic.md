###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_FadeOutMusic

Halt the music stream after fading it out for a specified time.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool Mix_FadeOutMusic(int ms);
```

## Function Parameters

|     |        |                                                            |
| --- | ------ | ---------------------------------------------------------- |
| int | **ms** | number of milliseconds to fade before halting the channel. |

## Return Value

(bool) Returns true if music was scheduled to fade, false otherwise. If no
music is currently playing, this returns false.

## Remarks

This will begin the music fading from its current volume to silence over
`ms` milliseconds. After that time, the music is halted.

Any halted music will call any callback specified by
[Mix_HookMusicFinished](Mix_HookMusicFinished)() once the halt occurs.

Fading music will change it's volume progressively, as if
[Mix_VolumeMusic](Mix_VolumeMusic)() was called on it (which is to say: you
probably shouldn't call [Mix_VolumeMusic](Mix_VolumeMusic)() on a fading
channel).

Note that this function does not block for the number of milliseconds
requested; it just schedules the music to fade and notes the time for the
mixer to manage later, and returns immediately.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

