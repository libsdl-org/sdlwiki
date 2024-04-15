###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FlashOperation

Window flash operation.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef enum SDL_FlashOperation
{
    SDL_FLASH_CANCEL,                   /**< Cancel any window flash state */
    SDL_FLASH_BRIEFLY,                  /**< Flash the window briefly to get attention */
    SDL_FLASH_UNTIL_FOCUSED             /**< Flash the window until it gets focus */
} SDL_FlashOperation;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

