###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_TextInputType

Text input type.

## Header File

Defined in [<SDL3/SDL_keyboard.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h)

## Syntax

```c
typedef enum SDL_TextInputType
{
    SDL_TEXTINPUT_TYPE_TEXT,                        /**< The input is text */
    SDL_TEXTINPUT_TYPE_TEXT_NAME,                   /**< The input is a person's name */
    SDL_TEXTINPUT_TYPE_TEXT_EMAIL,                  /**< The input is an e-mail address */
    SDL_TEXTINPUT_TYPE_TEXT_USERNAME,               /**< The input is a username */
    SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_HIDDEN,        /**< The input is a secure password that is hidden */
    SDL_TEXTINPUT_TYPE_TEXT_PASSWORD_VISIBLE,       /**< The input is a secure password that is visible */
    SDL_TEXTINPUT_TYPE_NUMBER,                      /**< The input is a number */
    SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_HIDDEN,      /**< The input is a secure PIN that is hidden */
    SDL_TEXTINPUT_TYPE_NUMBER_PASSWORD_VISIBLE      /**< The input is a secure PIN that is visible */
} SDL_TextInputType;
```

## Remarks

These are the valid values for
[SDL_PROP_TEXTINPUT_TYPE_NUMBER](SDL_PROP_TEXTINPUT_TYPE_NUMBER). Not every
value is valid on every platform, but where a value isn't supported, a
reasonable fallback will be used.

## Version

This enum is available since SDL 3.1.3.

## See Also

- [SDL_StartTextInputWithProperties](SDL_StartTextInputWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryKeyboard](CategoryKeyboard)

