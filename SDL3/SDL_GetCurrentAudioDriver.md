###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentAudioDriver

Get the name of the current audio driver.

## Header File

Defined in [<SDL3/SDL_audio.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_audio.h)

## Syntax

```c
const char* SDL_GetCurrentAudioDriver(void);
```

## Return Value

Returns the name of the current audio driver or NULL if no driver has been
initialized.

## Remarks

The names of drivers are all simple, low-ASCII identifiers, like "alsa",
"coreaudio" or "wasapi". These never have Unicode characters, and are not
meant to be proper names.

The returned string follows the [SDL_GetStringRule](SDL_GetStringRule).

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
const char* driver_name = SDL_GetCurrentAudioDriver();

if (driver_name) {
    printf("Audio subsystem initialized; driver = %s.\n", driver_name);
} else {
    printf("Audio subsystem not initialized.\n");
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAudio](CategoryAudio)

