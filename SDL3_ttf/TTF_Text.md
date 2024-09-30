###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_Text

Text created with [TTF_CreateText](TTF_CreateText)()

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef struct TTF_Text
{
    char *label;            /**< A label that you can allocate with SDL_strdup() for debugging purposes, and will be automatically freed in TTF_DestroyText(). */
    int w;                  /**< The width of this text, in pixels, read-only. */
    int h;                  /**< The height of this text, in pixels, read-only. */
    SDL_FColor color;       /**< The color of the text, read-write. You can change this anytime. */

    int refcount;           /**< Application reference count, used when freeing surface */

    TTF_TextData *internal; /**< Private */

} TTF_Text;
```

## Version

This struct is available since SDL_ttf 3.0.0.

## See Also

- [TTF_CreateText](TTF_CreateText)
- [TTF_CreateText_Wrapped](TTF_CreateText_Wrapped)
- [TTF_GetTextProperties](TTF_GetTextProperties)
- [TTF_DestroyText](TTF_DestroyText)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct)

