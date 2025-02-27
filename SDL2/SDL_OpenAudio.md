# SDL_OpenAudio

This function is a legacy means of opening the audio device.

## Header File

Defined in [SDL_audio.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_audio.h)

## Syntax

```c
int SDL_OpenAudio(SDL_AudioSpec * desired,
                  SDL_AudioSpec * obtained);
```

## Function Parameters

|                                  |              |                                                                                                                                                                                                                |
| -------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_AudioSpec](SDL_AudioSpec) * | **desired**  | an [SDL_AudioSpec](SDL_AudioSpec) structure representing the desired output format. Please refer to the [SDL_OpenAudioDevice](SDL_OpenAudioDevice) documentation for details on how to prepare this structure. |
| [SDL_AudioSpec](SDL_AudioSpec) * | **obtained** | an [SDL_AudioSpec](SDL_AudioSpec) structure filled in with the actual parameters, or NULL.                                                                                                                     |

## Return Value

(int) Returns 0 if successful, placing the actual hardware parameters in
the structure pointed to by `obtained`.

If `obtained` is NULL, the audio data passed to the callback function will
be guaranteed to be in the requested format, and will be automatically
converted to the actual hardware audio format if necessary. If `obtained`
is NULL, `desired` will have fields modified.

This function returns a negative error code on failure to open the audio
device or failure to set up the audio thread; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function remains for compatibility with SDL 1.2, but also because it's
slightly easier to use than the new functions in SDL 2.0. The new, more
powerful, and preferred way to do this is
[SDL_OpenAudioDevice](SDL_OpenAudioDevice)().

This function is roughly equivalent to:

```c
SDL_OpenAudioDevice(NULL, 0, desired, obtained, SDL_AUDIO_ALLOW_ANY_CHANGE);
```

With two notable exceptions:

- If `obtained` is NULL, we use `desired` (and allow no changes), which
  means desired will be modified to have the correct values for silence,
  etc, and SDL will convert any differences between your app's specific
  request and the hardware behind the scenes.
- The return value is always success or failure, and not a device ID, which
  means you can only have one device open at a time with this function.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CloseAudio](SDL_CloseAudio)
- [SDL_LockAudio](SDL_LockAudio)
- [SDL_PauseAudio](SDL_PauseAudio)
- [SDL_UnlockAudio](SDL_UnlockAudio)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

