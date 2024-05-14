###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LockAudio

This function is a legacy means of locking the audio device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
void SDL_LockAudio(void);

```

## Remarks

New programs might want to use [SDL_LockAudioDevice](SDL_LockAudioDevice)()
instead. This function is equivalent to calling...

```c
SDL_LockAudioDevice(1);
```

...and is only useful if you used the legacy
[SDL_OpenAudio](SDL_OpenAudio)() function.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_LockAudioDevice](SDL_LockAudioDevice)
- [SDL_UnlockAudio](SDL_UnlockAudio)
- [SDL_UnlockAudioDevice](SDL_UnlockAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

