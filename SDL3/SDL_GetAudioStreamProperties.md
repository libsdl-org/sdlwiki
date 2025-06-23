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

- [`SDL_PROP_AUDIOSTREAM_AUTO_CLEANUP_BOOLEAN`](SDL_PROP_AUDIOSTREAM_AUTO_CLEANUP_BOOLEAN):
  if true (the default), the stream be automatically cleaned up when the
  audio subsystem quits. If set to false, the streams will persist beyond
  that. This property is ignored for streams created through
  [SDL_OpenAudioDeviceStream](SDL_OpenAudioDeviceStream)(), and will always
  be cleaned up. Streams that are not cleaned up will still be unbound from
  devices when the audio subsystem quits. This property was added in SDL
  3.4.0.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

