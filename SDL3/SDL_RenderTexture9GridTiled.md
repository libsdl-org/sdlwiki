# SDL_RenderTexture9GridTiled

Perform a scaled copy using the 9-grid algorithm to the current rendering target at subpixel precision.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_RenderTexture9GridTiled(SDL_Renderer *renderer, SDL_Texture *texture, const SDL_FRect *srcrect, float left_width, float right_width, float top_height, float bottom_height, float scale, const SDL_FRect *dstrect, float tileScale);
```

## Function Parameters

|                                |                   |                                                                                                                                         |
| ------------------------------ | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Renderer](SDL_Renderer) * | **renderer**      | the renderer which should copy parts of a texture.                                                                                      |
| [SDL_Texture](SDL_Texture) *   | **texture**       | the source texture.                                                                                                                     |
| const [SDL_FRect](SDL_FRect) * | **srcrect**       | the [SDL_Rect](SDL_Rect) structure representing the rectangle to be used for the 9-grid, or NULL to use the entire texture.             |
| float                          | **left_width**    | the width, in pixels, of the left corners in `srcrect`.                                                                                 |
| float                          | **right_width**   | the width, in pixels, of the right corners in `srcrect`.                                                                                |
| float                          | **top_height**    | the height, in pixels, of the top corners in `srcrect`.                                                                                 |
| float                          | **bottom_height** | the height, in pixels, of the bottom corners in `srcrect`.                                                                              |
| float                          | **scale**         | the scale used to transform the corner of `srcrect` into the corner of `dstrect`, or 0.0f for an unscaled copy.                         |
| const [SDL_FRect](SDL_FRect) * | **dstrect**       | a pointer to the destination rectangle, or NULL for the entire rendering target.                                                        |
| float                          | **tileScale**     | the scale used to transform the borders and center of `srcrect` into the borders and middle of `dstrect`, or 1.0f for an unscaled copy. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The pixels in the texture are split into a 3x3 grid, using the different
corner sizes for each corner, and the sides and center making up the
remaining pixels. The corners are then scaled using `scale` and fit into
the corners of the destination rectangle. The sides and center are then
tiled into place to cover the remaining destination rectangle.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.4.0.

## See Also

- [SDL_RenderTexture](SDL_RenderTexture)
- [SDL_RenderTexture9Grid](SDL_RenderTexture9Grid)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

