###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DateTime

A structure holding a calendar date and time broken down into its components.

## Header File

Defined in [<SDL3/SDL_time.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_time.h)

## Syntax

```c
typedef struct SDL_DateTime
{
    int year;                  /**< Year */
    int month;                 /**< Month [01-12] */
    int day;                   /**< Day of the month [01-31] */
    int hour;                  /**< Hour [0-23] */
    int minute;                /**< Minute [0-59] */
    int second;                /**< Seconds [0-60] */
    int nanosecond;            /**< Nanoseconds [0-999999999] */
    int day_of_week;           /**< Day of the week [0-6] (0 being Sunday) */
    int utc_offset;            /**< Seconds east of UTC */
} SDL_DateTime;
```

## Version

This struct is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryTime](CategoryTime)

