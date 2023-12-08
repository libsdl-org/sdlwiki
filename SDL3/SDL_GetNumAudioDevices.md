###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetNumAudioDevices

Get the number of built-in audio devices.

## Syntax

```c
int SDL_GetNumAudioDevices(int iscapture);

```

## Function Parameters

|                   |                                                                         |
| ----------------- | ----------------------------------------------------------------------- |
| **iscapture**     | zero to request playback devices, non-zero to request recording devices |

## Return Value

Returns the number of available devices exposed by the current driver or -1
if an explicit list of devices can't be determined. A return value of -1
does not necessarily mean an error condition.

## Remarks

This function is only valid after successfully initializing the audio
subsystem.

Note that audio capture support is not implemented as of SDL 2.0.4, so the
`iscapture` parameter is for future expansion and should always be zero for
now.

This function will return -1 if an explicit list of devices can't be
determined. Returning -1 is not an error. For example, if SDL is set up to
talk to a remote audio server, it can't list every one available on the
Internet, but it will still allow a specific host to be specified in
[SDL_OpenAudioDevice](SDL_OpenAudioDevice.md)().

In many common cases, when this function returns a value <= 0, it can still
successfully open the default device (NULL for first argument of
[SDL_OpenAudioDevice](SDL_OpenAudioDevice.md)()).

This function may trigger a complete redetect of available hardware. It
should not be called for each iteration of a loop, but rather once at the
start of a loop:

```c
// Don't do this:
for (int i = 0; i < SDL_GetNumAudioDevices(0); i++)

// do this instead:
const int count = SDL_GetNumAudioDevices(0);
for (int i = 0; i < count; ++i) { do_something_here(); }
```

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
int i, count = SDL_GetNumAudioDevices(0);
for (i = 0; i < count; ++i) {
    printf("Audio device %d: %s\n", i, SDL_GetAudioDeviceName(i, 0));
}
```

## Related Functions

* [SDL_GetAudioDeviceName](SDL_GetAudioDeviceName.md)
* [SDL_OpenAudioDevice](SDL_OpenAudioDevice.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAudio](CategoryAudio.md)
