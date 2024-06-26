###### (This function is part of SDL_mixer, a separate library from SDL.)
# Mix_QuerySpec

Find out what the actual audio device parameters are.

## Header File

Defined in [<SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/SDL2/include/SDL_mixer.h)

## Syntax

```c
int Mix_QuerySpec(int *frequency, Uint16 *format, int *channels);
```

## Function Parameters

|          |               |                                                                    |
| -------- | ------------- | ------------------------------------------------------------------ |
| int *    | **frequency** | On return, will be filled with the audio device's frequency in Hz. |
| Uint16 * | **format**    | On return, will be filled with the audio device's format.          |
| int *    | **channels**  | On return, will be filled with the audio device's channel count.   |

## Return Value

(int) Returns 1 if the audio device has been opened, 0 otherwise.

## Remarks

If [Mix_OpenAudioDevice](Mix_OpenAudioDevice)() was called with
`allowed_changes` set to anything but zero, or
[Mix_OpenAudio](Mix_OpenAudio)() was used, some audio device settings may
be different from the application's request. This function will report what
the device is actually running at.

Note this is only important if the app intends to touch the audio buffers
being sent to the hardware directly. If an app just wants to play audio
files and let SDL_mixer handle the low-level details, this function can
probably be ignored.

If the audio device is not opened, this function will return 0.

## Version

This function is available since SDL_mixer 2.0.0.

## See Also

- [Mix_OpenAudio](Mix_OpenAudio)
- [Mix_OpenAudioDevice](Mix_OpenAudioDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

