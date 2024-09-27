###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetGlyphScript

Get the script used by a 32-bit codepoint.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetGlyphScript(Uint32 ch, char *script, size_t script_size);
```

## Function Parameters

|        |                 |                                                                     |
| ------ | --------------- | ------------------------------------------------------------------- |
| Uint32 | **ch**          | the character code to check.                                        |
| char * | **script**      | a pointer filled in with the script used by `ch`.                   |
| size_t | **script_size** | the size of the script buffer, which must be at least 5 characters. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The supplied script value will be a null-terminated string of exactly four
characters.

If SDL_ttf was not built with HarfBuzz support, this function returns
false.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

