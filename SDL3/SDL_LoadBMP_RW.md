###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LoadBMP_RW

Load a BMP image from a seekable SDL data stream.

## Syntax

```c
SDL_Surface* SDL_LoadBMP_RW(SDL_RWops *src, SDL_bool freesrc);

```

## Function Parameters

|                 |                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------- |
| **src**         | the data stream for the surface                                                                                     |
| **freesrc**     | if [SDL_TRUE](SDL_TRUE), calls [SDL_RWclose](SDL_RWclose)() on `src` before returning, even in the case of an error |

## Return Value

Returns a pointer to a new [SDL_Surface](SDL_Surface) structure or NULL if
there was an error; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The new surface should be freed with
[SDL_DestroySurface](SDL_DestroySurface)(). Not doing so will result in a
memory leak.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
const char *image_path = "myimage.bmp";

/* "rb" will "read binary" files */
SDL_RWops *file = SDL_RWFromFile(image_path, "rb");

/* freesrc is true so the file automatically closes */
SDL_Surface *image = SDL_LoadBMP_RW(file, SDL_TRUE);

/* Let the user know if the file failed to load */
if (!image) {
    printf("Failed to load image at %s: %s\n", image_path, SDL_GetError());
    return;
}

/* Do something with image here. */

/* Make sure to eventually release the surface resource */
SDL_DestroySurface(image);
```

## Related Functions

* [SDL_DestroySurface](SDL_DestroySurface)
* [SDL_LoadBMP](SDL_LoadBMP)
* [SDL_SaveBMP_RW](SDL_SaveBMP_RW)

----
[CategoryAPI](CategoryAPI), [CategorySurface](CategorySurface)


