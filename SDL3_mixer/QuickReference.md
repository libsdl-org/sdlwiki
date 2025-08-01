<!-- DO NOT EDIT THIS PAGE ON THE WIKI. IT WILL BE OVERWRITTEN BY WIKIHEADERS AND CHANGES WILL BE LOST! -->

# QuickReference

If you want to paste this into a text editor that can't handle
the fancy Unicode section headers, try using
[QuickReferenceNoUnicode](QuickReferenceNoUnicode) instead.

```c
// SDL3_mixer API Quick Reference
//
// https://libsdl.org/projects/SDL_mixer/
//
// The latest version of this document can be found at https://wiki.libsdl.org/SDL3_mixer/QuickReference
// Based on SDL_mixer version 3.1.0
//
// This can be useful in an IDE with search and syntax highlighting.
//
// Original idea for this document came from Dan Bechard (thanks!)
// ASCII art generated by: https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow (with modified 'S' for readability)


//  ██████╗ ██████╗  ██╗      ███╗   ███╗ ██╗ ██╗  ██╗ ███████╗ ██████╗
// ██╔════╝ ██╔══██╗ ██║      ████╗ ████║ ██║ ╚██╗██╔╝ ██╔════╝ ██╔══██╗
// ███████╗ ██║  ██║ ██║      ██╔████╔██║ ██║  ╚███╔╝  █████╗   ██████╔╝
// ╚════██║ ██║  ██║ ██║      ██║╚██╔╝██║ ██║  ██╔██╗  ██╔══╝   ██╔══██╗
// ██████╔╝ ██████╔╝ ███████╗ ██║ ╚═╝ ██║ ██║ ██╔╝ ██╗ ███████╗ ██║  ██║
// ╚═════╝  ╚═════╝  ╚══════╝ ╚═╝     ╚═╝ ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝

#define SDL_MIXER_MAJOR_VERSION                                                                                                          // The current major version of SDL_mixer headers.
#define SDL_MIXER_MINOR_VERSION                                                                                                          // The current minor version of the SDL_mixer headers.
#define SDL_MIXER_MICRO_VERSION                                                                                                          // The current micro (or patchlevel) version of the SDL_mixer headers.
#define SDL_MIXER_VERSION                                                                                                                // This is the current version number macro of the SDL_mixer headers.
#define SDL_MIXER_VERSION_ATLEAST(X, Y, Z)                                                                                               // This macro will evaluate to true if compiled with SDL_mixer at least X.Y.Z.
int MIX_Version(void);                                                                                                                   // Get the version of SDL_mixer that is linked against your program.
bool MIX_Init(void);                                                                                                                     // Initialize the SDL_mixer library.
void MIX_Quit(void);                                                                                                                     // Deinitialize the SDL_mixer library.
int MIX_GetNumAudioDecoders(void);                                                                                                       // Report the number of audio decoders available for use.
const char * MIX_GetAudioDecoder(int index);                                                                                             // Report the name of a specific audio decoders.
MIX_Mixer * MIX_CreateMixerDevice(SDL_AudioDeviceID devid, const SDL_AudioSpec *spec);                                                   // Create a mixer that plays sound directly to an audio device.
MIX_Mixer * MIX_CreateMixer(const SDL_AudioSpec *spec);                                                                                  // Create a mixer that generates audio to a memory buffer.
void MIX_DestroyMixer(MIX_Mixer *mixer);                                                                                                 // Free a mixer.
SDL_PropertiesID MIX_GetMixerProperties(MIX_Mixer *mixer);                                                                               // Get the properties associated with a mixer.
bool MIX_GetMixerFormat(MIX_Mixer *mixer, SDL_AudioSpec *spec);                                                                          // Get the audio format a mixer is generating.
MIX_Audio * MIX_LoadAudio_IO(MIX_Mixer *mixer, SDL_IOStream *io, bool predecode, bool closeio);                                          // Load audio for playback from an SDL_IOStream.
MIX_Audio * MIX_LoadAudio(MIX_Mixer *mixer, const char *path, bool predecode);                                                           // Load audio for playback from a file.
MIX_Audio * MIX_LoadAudioWithProperties(SDL_PropertiesID props);                                                                         // Load audio for playback through a collection of properties.
MIX_Audio * MIX_LoadRawAudio_IO(MIX_Mixer *mixer, SDL_IOStream *io, const SDL_AudioSpec *spec, bool closeio);                            // Load raw PCM data from an SDL_IOStream.
MIX_Audio * MIX_LoadRawAudio(MIX_Mixer *mixer, const void *data, size_t datalen, const SDL_AudioSpec *spec);                             // Load raw PCM data from a memory buffer.
MIX_Audio * MIX_LoadRawAudioNoCopy(MIX_Mixer *mixer, const void *data, size_t datalen, const SDL_AudioSpec *spec, bool free_when_done);  // Load raw PCM data from a memory buffer without making a copy.
MIX_Audio * MIX_CreateSineWaveAudio(MIX_Mixer *mixer, int hz, float amplitude);                                                          // Create a MIX_Audio that generates a sinewave.
SDL_PropertiesID MIX_GetAudioProperties(MIX_Audio *audio);                                                                               // Get the properties associated with a MIX_Audio.
Sint64 MIX_GetAudioDuration(MIX_Audio *audio);                                                                                           // Get the length of a MIX_Audio's playback in sample frames.
bool MIX_GetAudioFormat(MIX_Audio *audio, SDL_AudioSpec *spec);                                                                          // Query the initial audio format of a MIX_Audio.
void MIX_DestroyAudio(MIX_Audio *audio);                                                                                                 // Destroy the specified audio.
MIX_Track * MIX_CreateTrack(MIX_Mixer *mixer);                                                                                           // Create a new track on a mixer.
void MIX_DestroyTrack(MIX_Track *track);                                                                                                 // Destroy the specified track.
SDL_PropertiesID MIX_GetTrackProperties(MIX_Track *track);                                                                               // Get the properties associated with a track.
MIX_Mixer * MIX_GetTrackMixer(MIX_Track *track);                                                                                         // Get the MIX_Mixer that owns a MIX_Track.
bool MIX_SetTrackAudio(MIX_Track *track, MIX_Audio *audio);                                                                              // Set a MIX_Track's input to a MIX_Audio.
bool MIX_SetTrackAudioStream(MIX_Track *track, SDL_AudioStream *stream);                                                                 // Set a MIX_Track's input to an SDL_AudioStream.
bool MIX_SetTrackIOStream(MIX_Track *track, SDL_IOStream *io, bool closeio);                                                             // Set a MIX_Track's input to an SDL_IOStream.
bool MIX_TagTrack(MIX_Track *track, const char *tag);                                                                                    // Assign an arbitrary tag to a track.
void MIX_UntagTrack(MIX_Track *track, const char *tag);                                                                                  // Remove an arbitrary tag from a track.
bool MIX_SetTrackPlaybackPosition(MIX_Track *track, Sint64 frames);                                                                      // Seek a playing track to a new position in its input.
Sint64 MIX_GetTrackPlaybackPosition(MIX_Track *track);                                                                                   // Get the current input position of a playing track.
bool MIX_TrackLooping(MIX_Track *track);                                                                                                 // Query whether a given track is looping.
MIX_Audio * MIX_GetTrackAudio(MIX_Track *track);                                                                                         // Query the MIX_Audio assigned to a track.
SDL_AudioStream * MIX_GetTrackAudioStream(MIX_Track *track);                                                                             // Query the SDL_AudioStream assigned to a track.
Sint64 MIX_GetTrackRemaining(MIX_Track *track);                                                                                          // Return the number of sample frames remaining to be mixed in a track.
Sint64 MIX_TrackMSToFrames(MIX_Track *track, Sint64 ms);                                                                                 // Convert milliseconds to sample frames for a track's current format.
Sint64 MIX_TrackFramesToMS(MIX_Track *track, Sint64 frames);                                                                             // Convert sample frames for a track's current format to milliseconds.
Sint64 MIX_AudioMSToFrames(MIX_Audio *audio, Sint64 ms);                                                                                 // Convert milliseconds to sample frames for a MIX_Audio's format.
Sint64 MIX_AudioFramesToMS(MIX_Audio *audio, Sint64 frames);                                                                             // Convert sample frames for a MIX_Audio's format to milliseconds.
Sint64 MIX_MSToFrames(int sample_rate, Sint64 ms);                                                                                       // Convert milliseconds to sample frames at a specific sample rate.
Sint64 MIX_FramesToMS(int sample_rate, Sint64 frames);                                                                                   // Convert sample frames, at a specific sample rate, to milliseconds.
bool MIX_PlayTrack(MIX_Track *track, SDL_PropertiesID options);                                                                          // Start (or restart) mixing a track for playback.
bool MIX_PlayTag(MIX_Mixer *mixer, const char *tag, SDL_PropertiesID options);                                                           // Start (or restart) mixing all tracks with a specific tag for playback.
bool MIX_PlayAudio(MIX_Mixer *mixer, MIX_Audio *audio);                                                                                  // Play a MIX_Audio from start to finish without any management.
bool MIX_StopTrack(MIX_Track *track, Sint64 fade_out_frames);                                                                            // Halt a currently-playing track, possibly fading out over time.
bool MIX_StopAllTracks(MIX_Mixer *mixer, Sint64 fade_out_ms);                                                                            // Halt all currently-playing tracks, possibly fading out over time.
bool MIX_StopTag(MIX_Mixer *mixer, const char *tag, Sint64 fade_out_ms);                                                                 // Halt all tracks with a specific tag, possibly fading out over time.
bool MIX_PauseTrack(MIX_Track *track);                                                                                                   // Pause a currently-playing track.
bool MIX_PauseAllTracks(MIX_Mixer *mixer);                                                                                               // Pause all currently-playing tracks.
bool MIX_PauseTag(MIX_Mixer *mixer, const char *tag);                                                                                    // Pause all tracks with a specific tag.
bool MIX_ResumeTrack(MIX_Track *track);                                                                                                  // Resume a currently-paused track.
bool MIX_ResumeAllTracks(MIX_Mixer *mixer);                                                                                              // Resume all currently-paused tracks.
bool MIX_ResumeTag(MIX_Mixer *mixer, const char *tag);                                                                                   // Resume all tracks with a specific tag.
bool MIX_TrackPlaying(MIX_Track *track);                                                                                                 // Query if a track is currently playing.
bool MIX_TrackPaused(MIX_Track *track);                                                                                                  // Query if a track is currently paused.
bool MIX_SetMasterGain(MIX_Mixer *mixer, float gain);                                                                                    // Set a mixer's master gain control.
float MIX_GetMasterGain(MIX_Mixer *mixer);                                                                                               // Get a mixer's master gain control.
bool MIX_SetTrackGain(MIX_Track *track, float gain);                                                                                     // Set a track's gain control.
float MIX_GetTrackGain(MIX_Track *track);                                                                                                // Get a track's gain control.
bool MIX_SetTagGain(MIX_Mixer *mixer, const char *tag, float gain);                                                                      // Set the gain control of all tracks with a specific tag.
bool MIX_SetTrackFrequencyRatio(MIX_Track *track, float ratio);                                                                          // Change the frequency ratio of a track.
float MIX_GetTrackFrequencyRatio(MIX_Track *track);                                                                                      // Query the frequency ratio of a track.
bool MIX_SetTrackOutputChannelMap(MIX_Track *track, const int *chmap, int count);                                                        // Set the current output channel map of a track.
bool MIX_SetTrackStereo(MIX_Track *track, const MIX_StereoGains *gains);                                                                 // Force a track to stereo output, with optionally left/right panning.
bool MIX_SetTrack3DPosition(MIX_Track *track, const MIX_Point3D *position);                                                              // Set a track's position in 3D space.
bool MIX_GetTrack3DPosition(MIX_Track *track, MIX_Point3D *position);                                                                    // Get a track's current position in 3D space.
MIX_Group * MIX_CreateGroup(MIX_Mixer *mixer);                                                                                           // Create a mixing group.
void MIX_DestroyGroup(MIX_Group *group);                                                                                                 // Destroy a mixing group.
SDL_PropertiesID MIX_GetGroupProperties(MIX_Group *group);                                                                               // Get the properties associated with a group.
MIX_Mixer * MIX_GetGroupMixer(MIX_Group *group);                                                                                         // Get the MIX_Mixer that owns a MIX_Group.
bool MIX_SetTrackGroup(MIX_Track *track, MIX_Group *group);                                                                              // Assign a track to a mixing group.
bool MIX_SetTrackStoppedCallback(MIX_Track *track, MIX_TrackStoppedCallback cb, void *userdata);                                         // Set a callback that fires when a MIX_Track is stopped.
bool MIX_SetTrackRawCallback(MIX_Track *track, MIX_TrackMixCallback cb, void *userdata);                                                 // Set a callback that fires when a MIX_Track has initial decoded audio.
bool MIX_SetTrackCookedCallback(MIX_Track *track, MIX_TrackMixCallback cb, void *userdata);                                              // Set a callback that fires when the mixer has transformed a track's audio.
bool MIX_SetGroupPostMixCallback(MIX_Group *group, MIX_GroupMixCallback cb, void *userdata);                                             // Set a callback that fires when a mixer group has completed mixing.
bool MIX_SetPostMixCallback(MIX_Mixer *mixer, MIX_PostMixCallback cb, void *userdata);                                                   // Set a callback that fires when all mixing has completed.
bool MIX_Generate(MIX_Mixer *mixer, void *buffer, int buflen);                                                                           // Generate mixer output when not driving an audio device.
MIX_AudioDecoder * MIX_CreateAudioDecoder(const char *path, SDL_PropertiesID props);                                                     // Create a MIX_AudioDecoder from a path on the filesystem.
MIX_AudioDecoder * MIX_CreateAudioDecoder_IO(SDL_IOStream *io, bool closeio, SDL_PropertiesID props);                                    // Create a MIX_AudioDecoder from an SDL_IOStream.
void MIX_DestroyAudioDecoder(MIX_AudioDecoder *audiodecoder);                                                                            // Destroy the specified audio decoder.
SDL_PropertiesID MIX_GetAudioDecoderProperties(MIX_AudioDecoder *audiodecoder);                                                          // Get the properties associated with a MIX_AudioDecoder.
bool MIX_GetAudioDecoderFormat(MIX_AudioDecoder *audiodecoder, SDL_AudioSpec *spec);                                                     // Query the initial audio format of a MIX_AudioDecoder.
int MIX_DecodeAudio(MIX_AudioDecoder *audiodecoder, void *buffer, int buflen, const SDL_AudioSpec *spec);                                // Decode more audio from a MIX_AudioDecoder.
```

