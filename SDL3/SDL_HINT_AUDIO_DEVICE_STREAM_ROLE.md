# SDL_HINT_AUDIO_DEVICE_STREAM_ROLE

Specify an application role for an audio device.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUDIO_DEVICE_STREAM_ROLE "SDL_AUDIO_DEVICE_STREAM_ROLE"
```

## Remarks

Some audio backends (such as Pipewire) allow you to describe the role of
your audio stream. Among other things, this description might show up in a
system control panel or software for displaying and manipulating media
playback/recording graphs.

This hints lets you transmit that information to the OS. The contents of
this hint are used while opening an audio device. You should use a string
that describes your what your program is playing (Game, Music, Movie,
etc...).

Setting this to "" or leaving it unset will have SDL use a reasonable
default: "Game" or something similar.

Note that while this talks about audio streams, this is an OS-level
concept, so it applies to a physical audio device in this case, and not an
[SDL_AudioStream](SDL_AudioStream), nor an SDL logical audio device.

For Windows WASAPI audio, the following roles are supported, and map to
`AUDIO_STREAM_CATEGORY`:

- "Other" (default)
- "Communications" - Real-time communications, such as VOIP or chat
- "Game" - Game audio
- "GameChat" - Game chat audio, similar to "Communications" except that
  this will not attenuate other audio streams
- "Movie" - Music or sound with dialog
- "Media" - Music or sound without dialog

If your application applies its own echo cancellation, gain control, and
noise reduction it should also set
[SDL_HINT_AUDIO_DEVICE_RAW_STREAM](SDL_HINT_AUDIO_DEVICE_RAW_STREAM).

This hint should be set before an audio device is opened.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

