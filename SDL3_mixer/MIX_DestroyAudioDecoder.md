###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_DestroyAudioDecoder

Destroy the specified audio decoder.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
void MIX_DestroyAudioDecoder(MIX_AudioDecoder *audiodecoder);
```

## Function Parameters

|                                        |                  |                       |
| -------------------------------------- | ---------------- | --------------------- |
| [MIX_AudioDecoder](MIX_AudioDecoder) * | **audiodecoder** | the audio to destroy. |

## Remarks

Destroying a NULL [MIX_AudioDecoder](MIX_AudioDecoder) is a legal no-op.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

