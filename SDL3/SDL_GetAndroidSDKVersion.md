###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetAndroidSDKVersion

Query Android API level of the current device.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
int SDL_GetAndroidSDKVersion(void);
```

## Return Value

Returns the Android API level.

## Remarks

- API level 34: Android 14 (UPSIDE_DOWN_CAKE)
- API level 33: Android 13 (TIRAMISU)
- API level 32: Android 12L (S_V2)
- API level 31: Android 12 (S)
- API level 30: Android 11 (R)
- API level 29: Android 10 (Q)
- API level 28: Android 9 (P)
- API level 27: Android 8.1 (O_MR1)
- API level 26: Android 8.0 (O)
- API level 25: Android 7.1 (N_MR1)
- API level 24: Android 7.0 (N)
- API level 23: Android 6.0 (M)
- API level 22: Android 5.1 (LOLLIPOP_MR1)
- API level 21: Android 5.0 (LOLLIPOP, L)
- API level 20: Android 4.4W (KITKAT_WATCH)
- API level 19: Android 4.4 (KITKAT)
- API level 18: Android 4.3 (JELLY_BEAN_MR2)
- API level 17: Android 4.2 (JELLY_BEAN_MR1)
- API level 16: Android 4.1 (JELLY_BEAN)
- API level 15: Android 4.0.3 (ICE_CREAM_SANDWICH_MR1)
- API level 14: Android 4.0 (ICE_CREAM_SANDWICH)
- API level 13: Android 3.2 (HONEYCOMB_MR2)
- API level 12: Android 3.1 (HONEYCOMB_MR1)
- API level 11: Android 3.0 (HONEYCOMB)
- API level 10: Android 2.3.3 (GINGERBREAD_MR1)

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem), [CategoryAndroid](CategoryAndroid)


