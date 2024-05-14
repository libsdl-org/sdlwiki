###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FlashOperation

Window flash operation

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
typedef enum SDL_FlashOperation
{
    SDL_FLASH_CANCEL,                   /**< Cancel any window flash state */
    SDL_FLASH_BRIEFLY,                  /**< Flash the window briefly to get attention */
    SDL_FLASH_UNTIL_FOCUSED             /**< Flash the window until it gets focus */
} SDL_FlashOperation;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryVideo](CategoryVideo)

