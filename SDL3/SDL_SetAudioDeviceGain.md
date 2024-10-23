###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetAudioDeviceGain

Change the gain of an audio device.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
bool SDL_SetAudioDeviceGain(SDL_AudioDeviceID devid, float gain);
```

## Function Parameters

|                                        |           |                                               |
| -------------------------------------- | --------- | --------------------------------------------- |
| [SDL_AudioDeviceID](SDL_AudioDeviceID) | **devid** | the audio device on which to change gain.     |
| float                                  | **gain**  | the gain. 1.0f is no change, 0.0f is silence. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The gain of a device is its volume; a larger gain means a louder output,
with a gain of zero being silence.

Audio devices default to a gain of 1.0f (no change in output).

Physical devices may not have their gain changed, only logical devices, and
this function will always return false when used on physical devices. While
it might seem attractive to adjust several logical devices at once in this
way, it would allow an app or library to interfere with another portion of
the program's otherwise-isolated devices.

This is applied, along with any per-audiostream gain, during playback to
the hardware, and can be continuously changed to create various effects. On
recording devices, this will adjust the gain before passing the data into
an audiostream; that recording audiostream can then adjust its gain further
when outputting the data elsewhere, if it likes, but that second gain is
not applied until the data leaves the audiostream again.

## Thread Safety

It is safe to call this function from any thread, as it holds a
stream-specific mutex while running.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_GetAudioDeviceGain](SDL_GetAudioDeviceGain)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

