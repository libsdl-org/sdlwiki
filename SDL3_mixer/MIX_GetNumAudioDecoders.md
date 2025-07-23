###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetNumAudioDecoders

Report the number of audio decoders available for use.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int MIX_GetNumAudioDecoders(void);
```

## Return Value

(int) Returns the number of decoders available.

## Remarks

An audio decoder is what turns specific audio file formats into usable PCM
data. For example, there might be an MP3 decoder, or a WAV decoder, etc.
SDL_mixer probably has several decoders built in.

The return value can be used to call
[MIX_GetAudioDecoder](MIX_GetAudioDecoder)() in a loop.

The number of decoders available is decided during [MIX_Init](MIX_Init)()
and does not change until the library is deinitialized.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetAudioDecoder](MIX_GetAudioDecoder)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

