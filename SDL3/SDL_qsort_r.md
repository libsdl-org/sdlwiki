###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_qsort_r

Sort an array, passing a userdata pointer to the compare function.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_qsort_r(void *base, size_t nmemb, size_t size, SDL_CompareCallback_r compare, void *userdata);
```

## Function Parameters

|                                                |              |                                                   |
| ---------------------------------------------- | ------------ | ------------------------------------------------- |
| void *                                         | **base**     | a pointer to the start of the array.              |
| size_t                                         | **nmemb**    | the number of elements in the array.              |
| size_t                                         | **size**     | the size of the elements in the array.            |
| [SDL_CompareCallback_r](SDL_CompareCallback_r) | **compare**  | a function used to compare elements in the array. |
| void *                                         | **userdata** | a pointer to pass to the compare function.        |

## Remarks

For example:

```c
typedef enum {
    sort_increasing,
    sort_decreasing,
} sort_method;

typedef struct {
    int key;
    const char *string;
} data;

int SDLCALL compare(const void *userdata, const void *a, const void *b)
{
    sort_method method = (sort_method)(uintptr_t)userdata;
    const data *A = (const data *)a;
    const data *B = (const data *)b;

    if (A->key < B->key) {
        return (method == sort_increasing) ? -1 : 1;
    } else if (B->key < A->key) {
        return (method == sort_increasing) ? 1 : -1;
    } else {
        return 0;
    }
}

data values[] = {
    { 3, "third" }, { 1, "first" }, { 2, "second" }
};

SDL_qsort_r(values, SDL_arraysize(values), sizeof(values[0]), compare, (const void *)(uintptr_t)sort_increasing);
```

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_bsearch_r](SDL_bsearch_r)
- [SDL_qsort](SDL_qsort)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

