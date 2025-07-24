###### (This function is part of SDL_mixer, a separate library from SDL.)
# MIX_GetAudioProperties

Get the properties associated with a [MIX_Audio](MIX_Audio).

## Header File

Defined in [<SDL3_mixer/SDL_mixer.h>](https://github.com/libsdl-org/SDL_mixer/blob/main/include/SDL3_mixer/SDL_mixer.h)

## Syntax

```c
SDL_PropertiesID MIX_GetAudioProperties(MIX_Audio *audio);
```

## Function Parameters

|                          |           |                     |
| ------------------------ | --------- | ------------------- |
| [MIX_Audio](MIX_Audio) * | **audio** | the audio to query. |

## Return Value

(SDL_PropertiesID) Returns a valid property ID on success or 0 on failure;
call SDL_GetError() for more information.

## Remarks

SDL_mixer offers some properties of its own, but this can also be a
convenient place to store app-specific data.

A SDL_PropertiesID is created the first time this function is called for a
given [MIX_Audio](MIX_Audio), if necessary.

The following read-only properties are provided by SDL_mixer:

- [`MIX_PROP_METADATA_TITLE_STRING`](MIX_PROP_METADATA_TITLE_STRING): the
  audio's title ("Smells Like Teen Spirit").
- [`MIX_PROP_METADATA_ARTIST_STRING`](MIX_PROP_METADATA_ARTIST_STRING): the
  audio's artist name ("Nirvana").
- [`MIX_PROP_METADATA_ALBUM_STRING`](MIX_PROP_METADATA_ALBUM_STRING): the
  audio's album name ("Nevermind").
- [`MIX_PROP_METADATA_COPYRIGHT_STRING`](MIX_PROP_METADATA_COPYRIGHT_STRING):
  the audio's copyright info ("Copyright (c) 1991")
- [`MIX_PROP_METADATA_TRACK_NUMBER`](MIX_PROP_METADATA_TRACK_NUMBER): the
  audio's track number on the album (1)
- [`MIX_PROP_METADATA_TOTAL_TRACKS_NUMBER`](MIX_PROP_METADATA_TOTAL_TRACKS_NUMBER):
  the total tracks on the album (13)
- [`MIX_PROP_METADATA_YEAR_NUMBER`](MIX_PROP_METADATA_YEAR_NUMBER): the
  year the audio was released (1991)
- [`MIX_PROP_METADATA_DURATION_FRAMES_NUMBER`](MIX_PROP_METADATA_DURATION_FRAMES_NUMBER):
  The sample frames worth of PCM data that comprise this audio. It might be
  off by a little if the decoder only knows the duration as a unit of time.
- [`MIX_PROP_METADATA_DURATION_INFINITE_BOOLEAN`](MIX_PROP_METADATA_DURATION_INFINITE_BOOLEAN):
  if true, audio never runs out of sound to generate. This isn't
  necessarily always known to SDL_mixer, though.

Other properties, documented with
[MIX_LoadAudioWithProperties](MIX_LoadAudioWithProperties)(), may also be
present.

Note that the metadata properties are whatever SDL_mixer finds in things
like ID3 tags, and they often have very little standardized formatting, may
be missing, and can be completely wrong if the original data is
untrustworthy (like an MP3 from a P2P file sharing service).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_mixer 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLMixer](CategorySDLMixer)

