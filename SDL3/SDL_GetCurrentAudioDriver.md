###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetCurrentAudioDriver

Get the name of the current audio driver.

## Syntax

```c
const char* SDL_GetCurrentAudioDriver(void);

```

## Return Value

Returns the name of the current audio driver or NULL if no driver has been
initialized.

## Remarks

The returned string points to internal static memory and thus never becomes
invalid, even if you quit the audio subsystem and initialize a new driver
(although such a case would return a different static string from another
call to this function, of course). As such, you should not modify or free
the returned string.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
const char* driver_name = SDL_GetCurrentAudioDriver();

if (driver_name) {
    printf("Audio subsystem initialized; driver = %s.\n", driver_name);
} else {
    printf("Audio subsystem not initialized.\n");
}
```

----
[CategoryAPI](CategoryAPI.md), [CategoryAudio](CategoryAudio.md)
