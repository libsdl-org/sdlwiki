###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetAudioDecoderProperties

Get the properties associated with a [MIX_AudioDecoder](MIX_AudioDecoder).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
SDL_PropertiesID MIX_GetAudioDecoderProperties(MIX_AudioDecoder *audiodecoder);
```

## Function Parameters

|                                        |                  |                             |
| -------------------------------------- | ---------------- | --------------------------- |
| [MIX_AudioDecoder](MIX_AudioDecoder) * | **audiodecoder** | the audio decoder to query. |

## Return Value

(SDL_PropertiesID) Returns a valid property ID on success or 0 on failure;
call SDL_GetError() for more information.

## Remarks

SDL_mixer offers some properties of its own, but this can also be a
convenient place to store app-specific data.

A SDL_PropertiesID is created the first time this function is called for a
given [MIX_AudioDecoder](MIX_AudioDecoder), if necessary.

The file-specific metadata exposed through this function is identical to
those available through [MIX_GetAudioProperties](MIX_GetAudioProperties)().
Please refer to that function's documentation for details.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetAudioProperties](MIX_GetAudioProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

