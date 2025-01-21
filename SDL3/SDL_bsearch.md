###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_bsearch

Perform a binary search on a previously sorted array.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_bsearch(const void *key, const void *base, size_t nmemb, size_t size, SDL_CompareCallback compare);
```

## Function Parameters

|                                            |             |                                                             |
| ------------------------------------------ | ----------- | ----------------------------------------------------------- |
| const void *                               | **key**     | a pointer to a key equal to the element being searched for. |
| const void *                               | **base**    | a pointer to the start of the array.                        |
| size_t                                     | **nmemb**   | the number of elements in the array.                        |
| size_t                                     | **size**    | the size of the elements in the array.                      |
| [SDL_CompareCallback](SDL_CompareCallback) | **compare** | a function used to compare elements in the array.           |

## Return Value

(void *) Returns a pointer to the matching element in the array, or NULL if
not found.

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
    { 1, "first" }, { 2, "second" }, { 3, "third" }
};
data key = { 2, NULL };

data *result = SDL_bsearch(&key, values, SDL_arraysize(values), sizeof(values[0]), compare);
```

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_bsearch_r](SDL_bsearch_r)
- [SDL_qsort](SDL_qsort)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

