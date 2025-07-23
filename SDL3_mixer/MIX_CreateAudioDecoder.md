###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_CreateAudioDecoder

Create a [MIX_AudioDecoder](MIX_AudioDecoder) from a path on the filesystem.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
MIX_AudioDecoder * MIX_CreateAudioDecoder(const char *path, SDL_PropertiesID props);
```

## Function Parameters

|                  |           |                                                     |
| ---------------- | --------- | --------------------------------------------------- |
| const char *     | **path**  | the path on the filesystem from which to load data. |
| SDL_PropertiesID | **props** | decoder-specific properties. May be zero.           |

## Return Value

([MIX_AudioDecoder](MIX_AudioDecoder) *) Returns an audio decoder, ready to
decode.

## Remarks

Most apps won't need this, as SDL_mixer's usual interfaces will decode
audio as needed. However, if one wants to decode an audio file into a
memory buffer without playing it, this interface offers that.

This function allows properties to be specified. This is intended to supply
file-specific settings, such as where to find SoundFonts for a MIDI file,
etc. In most cases, the caller should pass a zero to specify no extra
properties.

When done with the audio decoder, it can be destroyed with
[MIX_DestroyAudioDecoder](MIX_DestroyAudioDecoder)().

This function requires SDL_mixer to have been initialized with a successful
call to [MIX_Init](MIX_Init)(), but does not need an actual
[MIX_Mixer](MIX_Mixer) to have been created.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_CreateAudioDecoder_IO](MIX_CreateAudioDecoder_IO)
- [MIX_DecodeAudio](MIX_DecodeAudio)
- [MIX_DestroyAudioDecoder](MIX_DestroyAudioDecoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

