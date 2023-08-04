###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAudioDriver

Use this function to get the name of a built in audio driver.

## Syntax

```c
const char* SDL_GetAudioDriver(int index);

```

## Function Parameters

|               |                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| **index**     | the index of the audio driver; the value ranges from 0 to [SDL_GetNumAudioDrivers](SDL_GetNumAudioDrivers)() - 1 |

## Return Value

Returns the name of the audio driver at the requested index, or NULL if an
invalid index was specified.

## Remarks

The list of audio drivers is given in the order that they are normally
initialized by default; the drivers that seem more reasonable to choose
first (as far as the SDL developers believe) are earlier in the list.

The names of drivers are all simple, low-ASCII identifiers, like "alsa",
"coreaudio" or "xaudio2". These never have Unicode characters, and are not
meant to be proper names.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
int i;

for (i = 0; i < SDL_GetNumAudioDrivers(); ++i) {
    printf("Audio driver %d: %s\n", i, SDL_GetAudioDriver(i));
}
```

## Related Functions

* [SDL_GetNumAudioDrivers](SDL_GetNumAudioDrivers)

----
[CategoryAPI](CategoryAPI), [CategoryAudio](CategoryAudio)


