###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetTicks

Get the number of milliseconds since SDL library initialization.

## Syntax

```c
Uint64 SDL_GetTicks(void);

```

## Return Value

Returns an unsigned 64-bit value representing the number of milliseconds
since the SDL library initialized.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
unsigned int lastTime = 0, currentTime;
while (!quit) {
  // do stuff
  // ...

  // Print a report once per second
  currentTime = SDL_GetTicks();
  if (currentTime > lastTime + 1000) {
    printf("Report: %d\n", variable);
    lastTime = currentTime;
  }
}
```

----
[CategoryAPI](CategoryAPI), [CategoryTimer](CategoryTimer)


