###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetAudioDecoder

Report the name of a specific audio decoders.

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
const char * MIX_GetAudioDecoder(int index);
```

## Function Parameters

|     |           |                                    |
| --- | --------- | ---------------------------------- |
| int | **index** | the index of the decoder to query. |

## Return Value

(const char *) Returns a UTF-8 (really, ASCII) string of the decoder's
name, or NULL if `index` is invalid.

## Remarks

An audio decoder is what turns specific audio file formats into usable PCM
data. For example, there might be an MP3 decoder, or a WAV decoder, etc.
SDL_mixer probably has several decoders built in.

The names are capital English letters and numbers, low-ASCII. They don't
necessarily map to a specific file format; Some decoders, like "XMP"
operate on multiple file types, and more than one decoder might handle the
same file type, like "DRMP3" vs "MPG123". Note that in that last example,
neither decoder is called "MP3".

The index of a specific decoder is decided during [MIX_Init](MIX_Init)()
and does not change until the library is deinitialized. Valid indices are
between zero and the return value of
[MIX_GetNumAudioDecoders](MIX_GetNumAudioDecoders)().

The returned pointer is const memory owned by SDL_mixer; do not free it.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

## See Also

- [MIX_GetNumAudioDecoders](MIX_GetNumAudioDecoders)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

