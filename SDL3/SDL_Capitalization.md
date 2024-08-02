###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Capitalization

Auto capitalization type.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
typedef enum SDL_Capitalization
{
    SDL_CAPITALIZE_NONE,        /**< No auto-capitalization will be done */
    SDL_CAPITALIZE_SENTENCES,   /**< The first letter of sentences will be capitalized */
    SDL_CAPITALIZE_WORDS,       /**< The first letter of words will be capitalized */
    SDL_CAPITALIZE_LETTERS      /**< All letters will be capitalized */
} SDL_Capitalization;
```

## Remarks

These are the valid values for
[SDL_PROP_TEXTINPUT_AUTOCAPITALIZATION_NUMBER](SDL_PROP_TEXTINPUT_AUTOCAPITALIZATION_NUMBER).
Not every value is valid on every platform, but where a value isn't
supported, a reasonable fallback will be used.

## Version

This enum is available since SDL 3.0.0.

## See Also

- [SDL_StartTextInputWithProperties](SDL_StartTextInputWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryKeyboard](CategoryKeyboard)

