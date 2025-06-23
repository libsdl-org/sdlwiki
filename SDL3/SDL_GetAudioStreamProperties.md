# SDL_GetAudioStreamProperties

Get the properties associated with an audio stream.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
SDL_PropertiesID SDL_GetAudioStreamProperties(SDL_AudioStream *stream);
```

## Function Parameters

|                                      |            |                                                  |
| ------------------------------------ | ---------- | ------------------------------------------------ |
| [SDL_AudioStream](SDL_AudioStream) * | **stream** | the [SDL_AudioStream](SDL_AudioStream) to query. |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The application can hang any data it wants here, but the following
properties are understood by SDL:

- [`SDL_PROP_AUDIOSTREAM_KEEP_ON_SHUTDOWN_BOOLEAN`](SDL_PROP_AUDIOSTREAM_KEEP_ON_SHUTDOWN_BOOLEAN):
  if true, the stream will not be automatically destroyed during
  [SDL_Quit](SDL_Quit)(). This property is ignored for streams created
  through [SDL_OpenAudioDeviceStream](SDL_OpenAudioDeviceStream)(). Streams
  bound to devices that aren't destroyed will still be unbound. Default
  false. (since SDL 3.4.0)

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

