###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_Generate

Generate mixer output when not driving an audio device.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
bool MIX_Generate(MIX_Mixer *mixer, void *buffer, int buflen);
```

## Function Parameters

|                          |            |                                             |
| ------------------------ | ---------- | ------------------------------------------- |
| [MIX_Mixer](MIX_Mixer) * | **mixer**  | the mixer for which to generate more audio. |
| void *                   | **buffer** | a pointer to a buffer to store audio in.    |
| int                      | **buflen** | the number of bytes to store in buffer.     |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

SDL_mixer allows the creation of [MIX_Mixer](MIX_Mixer) objects that are
not connected to an audio device, by calling
[MIX_CreateMixer](MIX_CreateMixer)() instead of
[MIX_CreateMixerDevice](MIX_CreateMixerDevice)(). Such mixers will not
generate output until explicitly requested through this function.

The caller may request as much audio as desired, so long as `buflen` is a
multiple of the sample frame size specified when creating the mixer (for
example, if requesting stereo Sint16 audio, buflen must be a multiple of 4:
2 bytes-per-channel times 2 channels).

The mixer will mix as quickly as possible; since it works in sample frames
instead of time, it can potentially generate enormous amounts of audio in a
small amount of time.

On success, this always fills `buffer` with `buflen` bytes of audio; if all
playing tracks finish mixing, it will fill the remaining buffer with
silence.

Each call to this function will pick up where it left off, playing tracks
will continue to mix from the point the previous call completed, etc. The
mixer state can be changed between each call in any way desired: tracks can
be added, played, stopped, changed, removed, etc. Effectively this function
does the same thing SDL_mixer does internally when the audio device needs
more audio to play.

This function can not be used with mixers from
[MIX_CreateMixerDevice](MIX_CreateMixerDevice)(); those generate audio as
needed internally.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_CreateMixer](MIX_CreateMixer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

