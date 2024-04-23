###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LoadBMP

Load a surface from a file.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
#define SDL_LoadBMP(file)   SDL_LoadBMP_RW(SDL_RWFromFile(file, "rb"), 1)
```

## Remarks

Convenience macro.

## Code Examples

```c++
const char *image_path = "myimage.bmp";
SDL_Surface *image = SDL_LoadBMP(image_path);

/* Let the user know if the file failed to load */
if (!image) {
    printf("Failed to load image at %s: %s\n", image_path, SDL_GetError());
    return 1;
}

/* Do something with image here. */

/* Make sure to eventually release the surface resource */
SDL_FreeSurface(image);
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySurface](CategorySurface)


