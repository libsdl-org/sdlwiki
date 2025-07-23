###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_DecodeAudio

Decode more audio from a [MIX_AudioDecoder](MIX_AudioDecoder).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
int MIX_DecodeAudio(MIX_AudioDecoder *audiodecoder, void *buffer, int buflen, const SDL_AudioSpec *spec);
```

## Function Parameters

|                                        |                  |                                                        |
| -------------------------------------- | ---------------- | ------------------------------------------------------ |
| [MIX_AudioDecoder](MIX_AudioDecoder) * | **audiodecoder** | the decoder from which to retrieve more data.          |
| void *                                 | **buffer**       | the memory buffer to store decoded audio.              |
| int                                    | **buflen**       | the maximum number of bytes to store to `buffer`.      |
| const SDL_AudioSpec *                  | **spec**         | the format that audio data will be stored to `buffer`. |

## Return Value

(int) Returns number of bytes decoded, or -1 on error; call SDL_GetError()
for more information.

## Remarks

Data is decoded on demand in whatever format is requested. The format is
permitted to change between calls.

This function will return the number of bytes decoded, which may be less
than requested if there was an error or end-of-file. A return value of zero
means the entire file was decoded, -1 means an unrecoverable error
happened.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

