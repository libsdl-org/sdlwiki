# CategorySDLMixer

SDL_mixer is a library to make complicated audio processing tasks easier.

It offers audio file decoding, mixing multiple sounds together, basic 3D
positional audio, and various audio effects.

It can mix sound to multiple audio devices in real time, or generate mixed
audio data to a memory buffer for any other use. It can do both at the same
time!

To use the library, first call [MIX_Init](MIX_Init)(). Then create a mixer
with [MIX_CreateMixerDevice](MIX_CreateMixerDevice)() (or
[MIX_CreateMixer](MIX_CreateMixer)() to render to memory).

Once you have a mixer, you can load sound data with
[MIX_LoadAudio](MIX_LoadAudio)(), [MIX_LoadAudio_IO](MIX_LoadAudio_IO)(),
or [MIX_LoadAudioWithProperties](MIX_LoadAudioWithProperties)(). Data gets
loaded once and can be played over and over.

When loading audio, SDL_mixer can parse out several metadata tag formats,
such as ID3 and APE tags, and exposes this information through the
[MIX_GetAudioProperties](MIX_GetAudioProperties)() function.

To play audio, you create a track with
[MIX_CreateTrack](MIX_CreateTrack)(). You need one track for each sound
that will be played simultaneously; think of tracks as individual sliders
on a mixer board. You might have loaded hundreds of audio files, but you
probably only have a handful of tracks that you assign those loaded files
to when they are ready to play, and reuse those tracks with different audio
later. Tracks take their input from a [MIX_Audio](MIX_Audio) (static data
to be played multiple times) or an SDL_AudioStream (streaming PCM audio the
app supplies, possibly as needed). A third option is to supply an
SDL_IOStream, to load and decode on the fly, which might be more efficient
for background music that is only used once, etc.

Assign input to a [MIX_Track](MIX_Track) with
[MIX_SetTrackAudio](MIX_SetTrackAudio)(),
[MIX_SetTrackAudioStream](MIX_SetTrackAudioStream)(), or
[MIX_SetTrackIOStream](MIX_SetTrackIOStream)().

Once a track has an input, start it playing with
[MIX_PlayTrack](MIX_PlayTrack)(). There are many options to this function
to dictate mixing features: looping, fades, etc.

Tracks can be tagged with arbitrary strings, like "music" or "ingame" or
"ui". These tags can be used to start, stop, and pause a selection of
tracks at the same moment.

All significant portions of the mixing pipeline have callbacks, so that an
app can hook in to the appropriate locations to examine or modify audio
data as it passes through the mixer: a "raw" callback for raw PCM data
decoded from an audio file without any modifications, a "cooked" callback
for that same data after all transformations (fade, positioning, etc) have
been processed, a "stopped" callback for when the track finishes mixing, a
"postmix" callback for the final mixed audio about to be sent to the audio
hardware to play. Additionally, you can use [MIX_Group](MIX_Group) objects
to mix a subset of playing tracks and access the data before it is mixed in
with other tracks. All of this is optional, but allows for powerful access
and control of the mixing process.

SDL_mixer can also be used for decoding audio files without actually
rendering a mix. This is done with [MIX_AudioDecoder](MIX_AudioDecoder).
Even though SDL_mixer handles decoding transparently when used as the audio
engine for an app, and probably won't need this interface in that normal
scenario, this can be useful when using a different audio library to access
many file formats.

This library offers several features on top of mixing sounds together: a
track can have its own gain, to adjust its volume, in addition to a master
gain applied as well. One can set the "frequency ratio" of a track, to
speed it up or slow it down, which also adjusts its pitch. A channel map
can also be applied per-track, to change what speaker a given channel of
audio is output to.

Almost all timing in SDL_mixer is in _sample frames_. Stereo PCM audio data
in Sint16 format takes 4 bytes per sample frame (2 bytes per sample times 2
channels), for example. This allows everything in SDL_mixer to run at
sample-perfect accuracy, and it lets it run without concern for wall clock
time--you can produce audio faster than real-time, if desired. The problem,
though, is different pieces of audio at different _sample rates_ will
produce a different number of sample frames for the same length of time. To
deal with this, conversion routines are offered:
[MIX_TrackMSToFrames](MIX_TrackMSToFrames)(),
[MIX_TrackFramesToMS](MIX_TrackFramesToMS)(), etc. Functions that operate
on multiple tracks at once will deal with time in milliseconds, so it can
do these conversions internally; be sure to read the documentation for
these small quirks!

SDL_mixer offers basic positional audio: a simple 3D positioning API
through [MIX_SetTrack3DPosition](MIX_SetTrack3DPosition)() and
[MIX_SetTrackStereo](MIX_SetTrackStereo)(). The former will do simple
distance attenuation and spatialization--on a stereo setup, you will hear
sounds move from left to right--and on a surround-sound configuration,
individual tracks can move around the user. The latter,
[MIX_SetTrackStereo](MIX_SetTrackStereo)(), will force a sound to the Front
Left and Front Right speakers and let the app pan it left and right as
desired. Either effect can be useful for different situations. SDL_mixer is
not meant to be a full 3D audio engine, but rather Good Enough for many
purposes; if something more powerful in terms of 3D audio is needed,
consider a proper 3D library like OpenAL.

<!-- END CATEGORY DOCUMENTATION -->

## Functions

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySDLMixer, CategoryAPIFunction -->
- [Mix_AllocateChannels](Mix_AllocateChannels)
- [Mix_ChannelFinished](Mix_ChannelFinished)
- [Mix_CloseAudio](Mix_CloseAudio)
- [Mix_EachSoundFont](Mix_EachSoundFont)
- [Mix_ExpireChannel](Mix_ExpireChannel)
- [Mix_FadeInChannel](Mix_FadeInChannel)
- [Mix_FadeInChannelTimed](Mix_FadeInChannelTimed)
- [Mix_FadeInMusic](Mix_FadeInMusic)
- [Mix_FadeInMusicPos](Mix_FadeInMusicPos)
- [Mix_FadeOutChannel](Mix_FadeOutChannel)
- [Mix_FadeOutGroup](Mix_FadeOutGroup)
- [Mix_FadeOutMusic](Mix_FadeOutMusic)
- [Mix_FadingChannel](Mix_FadingChannel)
- [Mix_FadingMusic](Mix_FadingMusic)
- [Mix_FreeChunk](Mix_FreeChunk)
- [Mix_FreeMusic](Mix_FreeMusic)
- [Mix_GetChunk](Mix_GetChunk)
- [Mix_GetChunkDecoder](Mix_GetChunkDecoder)
- [Mix_GetMusicAlbumTag](Mix_GetMusicAlbumTag)
- [Mix_GetMusicArtistTag](Mix_GetMusicArtistTag)
- [Mix_GetMusicCopyrightTag](Mix_GetMusicCopyrightTag)
- [Mix_GetMusicDecoder](Mix_GetMusicDecoder)
- [Mix_GetMusicHookData](Mix_GetMusicHookData)
- [Mix_GetMusicLoopEndTime](Mix_GetMusicLoopEndTime)
- [Mix_GetMusicLoopLengthTime](Mix_GetMusicLoopLengthTime)
- [Mix_GetMusicLoopStartTime](Mix_GetMusicLoopStartTime)
- [Mix_GetMusicPosition](Mix_GetMusicPosition)
- [Mix_GetMusicTitle](Mix_GetMusicTitle)
- [Mix_GetMusicTitleTag](Mix_GetMusicTitleTag)
- [Mix_GetMusicType](Mix_GetMusicType)
- [Mix_GetMusicVolume](Mix_GetMusicVolume)
- [Mix_GetNumChunkDecoders](Mix_GetNumChunkDecoders)
- [Mix_GetNumMusicDecoders](Mix_GetNumMusicDecoders)
- [Mix_GetNumTracks](Mix_GetNumTracks)
- [Mix_GetSoundFonts](Mix_GetSoundFonts)
- [Mix_GetTimidityCfg](Mix_GetTimidityCfg)
- [Mix_GroupAvailable](Mix_GroupAvailable)
- [Mix_GroupChannel](Mix_GroupChannel)
- [Mix_GroupChannels](Mix_GroupChannels)
- [Mix_GroupCount](Mix_GroupCount)
- [Mix_GroupNewer](Mix_GroupNewer)
- [Mix_GroupOldest](Mix_GroupOldest)
- [Mix_HaltChannel](Mix_HaltChannel)
- [Mix_HaltGroup](Mix_HaltGroup)
- [Mix_HaltMusic](Mix_HaltMusic)
- [Mix_HasChunkDecoder](Mix_HasChunkDecoder)
- [Mix_HasMusicDecoder](Mix_HasMusicDecoder)
- [Mix_HookMusic](Mix_HookMusic)
- [Mix_HookMusicFinished](Mix_HookMusicFinished)
- [Mix_Init](Mix_Init)
- [Mix_LoadMUS](Mix_LoadMUS)
- [Mix_LoadMUS_IO](Mix_LoadMUS_IO)
- [Mix_LoadMUSType_IO](Mix_LoadMUSType_IO)
- [Mix_LoadWAV](Mix_LoadWAV)
- [Mix_LoadWAV_IO](Mix_LoadWAV_IO)
- [Mix_MasterVolume](Mix_MasterVolume)
- [Mix_ModMusicJumpToOrder](Mix_ModMusicJumpToOrder)
- [Mix_MusicDuration](Mix_MusicDuration)
- [Mix_OpenAudio](Mix_OpenAudio)
- [Mix_Pause](Mix_Pause)
- [Mix_PauseAudio](Mix_PauseAudio)
- [Mix_Paused](Mix_Paused)
- [Mix_PausedMusic](Mix_PausedMusic)
- [Mix_PauseGroup](Mix_PauseGroup)
- [Mix_PauseMusic](Mix_PauseMusic)
- [Mix_PlayChannel](Mix_PlayChannel)
- [Mix_PlayChannelTimed](Mix_PlayChannelTimed)
- [Mix_Playing](Mix_Playing)
- [Mix_PlayingMusic](Mix_PlayingMusic)
- [Mix_PlayMusic](Mix_PlayMusic)
- [Mix_QuerySpec](Mix_QuerySpec)
- [Mix_QuickLoad_RAW](Mix_QuickLoad_RAW)
- [Mix_QuickLoad_WAV](Mix_QuickLoad_WAV)
- [Mix_Quit](Mix_Quit)
- [Mix_RegisterEffect](Mix_RegisterEffect)
- [Mix_ReserveChannels](Mix_ReserveChannels)
- [Mix_Resume](Mix_Resume)
- [Mix_ResumeGroup](Mix_ResumeGroup)
- [Mix_ResumeMusic](Mix_ResumeMusic)
- [Mix_RewindMusic](Mix_RewindMusic)
- [Mix_SetDistance](Mix_SetDistance)
- [Mix_SetMusicPosition](Mix_SetMusicPosition)
- [Mix_SetPanning](Mix_SetPanning)
- [Mix_SetPosition](Mix_SetPosition)
- [Mix_SetPostMix](Mix_SetPostMix)
- [Mix_SetReverseStereo](Mix_SetReverseStereo)
- [Mix_SetSoundFonts](Mix_SetSoundFonts)
- [Mix_SetTimidityCfg](Mix_SetTimidityCfg)
- [Mix_StartTrack](Mix_StartTrack)
- [Mix_UnregisterAllEffects](Mix_UnregisterAllEffects)
- [Mix_UnregisterEffect](Mix_UnregisterEffect)
- [Mix_Version](Mix_Version)
- [Mix_Volume](Mix_Volume)
- [Mix_VolumeChunk](Mix_VolumeChunk)
- [Mix_VolumeMusic](Mix_VolumeMusic)
<!-- END CATEGORY LIST -->

## Datatypes

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySDLMixer, CategoryAPIDatatype -->
- [Mix_EffectDone_t](Mix_EffectDone_t)
- [Mix_EffectFunc_t](Mix_EffectFunc_t)
- [MIX_InitFlags](MIX_InitFlags)
- [Mix_Music](Mix_Music)
<!-- END CATEGORY LIST -->

## Structs

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySDLMixer, CategoryAPIStruct -->
- [Mix_Chunk](Mix_Chunk)
<!-- END CATEGORY LIST -->

## Enums

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySDLMixer, CategoryAPIEnum -->
- [Mix_Fading](Mix_Fading)
- [MIX_InitFlags](MIX_InitFlags)
- [Mix_MusicType](Mix_MusicType)
<!-- END CATEGORY LIST -->

## Macros

<!-- DO NOT HAND-EDIT CATEGORY LISTS, THEY ARE AUTOGENERATED AND WILL BE OVERWRITTEN, BASED ON TAGS IN INDIVIDUAL PAGE FOOTERS. EDIT THOSE INSTEAD. -->
<!-- BEGIN CATEGORY LIST: CategorySDLMixer, CategoryAPIMacro -->
- [MIX_CHANNEL_POST](MIX_CHANNEL_POST)
- [MIX_EFFECTSMAXSPEED](MIX_EFFECTSMAXSPEED)
- [SDL_MIXER_MAJOR_VERSION](SDL_MIXER_MAJOR_VERSION)
- [SDL_MIXER_VERSION](SDL_MIXER_VERSION)
- [SDL_MIXER_VERSION_ATLEAST](SDL_MIXER_VERSION_ATLEAST)
<!-- END CATEGORY LIST -->

----
[CategoryAPICategory](CategoryAPICategory)

