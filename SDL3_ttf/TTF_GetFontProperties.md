###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontProperties

Get the properties associated with a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_PropertiesID TTF_GetFontProperties(TTF_Font *font);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(SDL_PropertiesID) Returns a valid property ID on success or 0 on failure;
call SDL_GetError() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

