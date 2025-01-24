# SDL_bsearch_r

Perform a binary search on a previously sorted array, passing a userdata pointer to the compare function.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_bsearch_r(const void *key, const void *base, size_t nmemb, size_t size, SDL_CompareCallback_r compare, void *userdata);
```

## Function Parameters

|                                                |              |                                                             |
| ---------------------------------------------- | ------------ | ----------------------------------------------------------- |
| const void *                                   | **key**      | a pointer to a key equal to the element being searched for. |
| const void *                                   | **base**     | a pointer to the start of the array.                        |
| size_t                                         | **nmemb**    | the number of elements in the array.                        |
| size_t                                         | **size**     | the size of the elements in the array.                      |
| [SDL_CompareCallback_r](SDL_CompareCallback_r) | **compare**  | a function used to compare elements in the array.           |
| void *                                         | **userdata** | a pointer to pass to the compare function.                  |

## Return Value

(void *) Returns a pointer to the matching element in the array, or NULL if
not found.

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
    { 1, "first" }, { 2, "second" }, { 3, "third" }
};
data key = { 2, NULL };

data *result = SDL_bsearch_r(&key, values, SDL_arraysize(values), sizeof(values[0]), compare, (const void *)(uintptr_t)sort_increasing);
```

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_bsearch](SDL_bsearch)
- [SDL_qsort_r](SDL_qsort_r)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

