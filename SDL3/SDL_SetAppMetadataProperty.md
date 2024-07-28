###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAppMetadataProperty

Specify metadata about your app through a set of properties.

## Header File

Defined in [<SDL3/SDL_init.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_init.h)

## Syntax

```c
int SDL_SetAppMetadataProperty(const char *name, const char *value);
```

## Function Parameters

|              |           |                                                             |
| ------------ | --------- | ----------------------------------------------------------- |
| const char * | **name**  | the name of the metadata property to set.                   |
| const char * | **value** | the value of the property, or NULL to remove that property. |

## Return Value

(int) Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You can optionally provide metadata about your app to SDL. This is not
required, but strongly encouraged.

There are several locations where SDL can make use of metadata (an "About"
box in the macOS menu bar, the name of the app can be shown on some audio
mixers, etc). Any piece of metadata can be left out, if a specific detail
doesn't make sense for the app.

This function should be called as early as possible, before
[SDL_Init](SDL_Init). Multiple calls to this function are allowed, but
various state might not change once it has been set up with a previous call
to this function.

Once set, this metadata can be read using
[SDL_GetMetadataProperty](SDL_GetMetadataProperty)().

These are the supported properties:

- [`SDL_PROP_APP_METADATA_NAME_STRING`](SDL_PROP_APP_METADATA_NAME_STRING):
  The human-readable name of the application, like "My Game 2: Bad Guy's
  Revenge!". This defaults to "SDL Application".
- [SDL_PROP_APP_METADATA_VERSION_STRING](SDL_PROP_APP_METADATA_VERSION_STRING)`:
  The version of the app that is running; there are no rules on format, so
  "1.0.3beta2" and "April 22nd, 2024" and a git hash are all valid options.
  This has no default.
- `[SDL_PROP_APP_METADATA_IDENTIFIER_STRING](SDL_PROP_APP_METADATA_IDENTIFIER_STRING)`:
  A unique string that identifies this app. This must be in reverse-domain
  format, like "com.example.mygame2". This string is used by desktop
  compositors to identify and group windows together, as well as match
  applications with associated desktop settings and icons. This has no
  default.
- SDL_PROP_APP_METADATA_CREATOR_STRING`: The human-readable name of the
  creator/developer/maker of this app, like "MojoWorkshop, LLC"
- [SDL_PROP_APP_METADATA_COPYRIGHT_STRING](SDL_PROP_APP_METADATA_COPYRIGHT_STRING)`:
  The human-readable copyright notice, like "Copyright (c) 2024
  MojoWorkshop, LLC" or whatnot. Keep this to one line, don't paste a copy
  of a whole software license in here. This has no default.
- SDL_PROP_APP_METADATA_URL_STRING`: A URL to the app on the web. Maybe a
  product page, or a storefront, or even a GitHub repository, for user's
  further information This has no default.
- [SDL_PROP_APP_METADATA_TYPE_STRING](SDL_PROP_APP_METADATA_TYPE_STRING)`:
  The type of application this is. Currently this string can be "game" for
  a video game, "mediaplayer" for a media player, or generically
  "application" if nothing else applies. Future versions of SDL might add
  new types. This defaults to "application".

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAppMetadataProperty](SDL_GetAppMetadataProperty)
- [SDL_SetAppMetadata](SDL_SetAppMetadata)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryInit](CategoryInit)

