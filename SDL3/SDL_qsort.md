###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_qsort

Sort an array.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_qsort(void *base, size_t nmemb, size_t size, SDL_CompareCallback compare);
```

## Function Parameters

|                                            |             |                                                   |
| ------------------------------------------ | ----------- | ------------------------------------------------- |
| void *                                     | **base**    | a pointer to the start of the array.              |
| size_t                                     | **nmemb**   | the number of elements in the array.              |
| size_t                                     | **size**    | the size of the elements in the array.            |
| [SDL_CompareCallback](SDL_CompareCallback) | **compare** | a function used to compare elements in the array. |

## Remarks

For example:

```c
typedef struct {
    int key;
    const char *string;
} data;

int SDLCALL compare(const void *a, const void *b)
{
    const data *A = (const data *)a;
    const data *B = (const data *)b;

    if (A->n < B->n) {
        return -1;
    } else if (B->n < A->n) {
        return 1;
    } else {
        return 0;
    }
}

data values[] = {
    { 3, "third" }, { 1, "first" }, { 2, "second" }
};

SDL_qsort(values, SDL_arraysize(values), sizeof(values[0]), compare);
```

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_bsearch](SDL_bsearch)
- [SDL_qsort_r](SDL_qsort_r)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

