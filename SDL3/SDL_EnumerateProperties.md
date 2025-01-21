###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_EnumerateProperties

Enumerate the properties contained in a group of properties.

## Header File

Defined in [<SDL3/SDL_properties.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_properties.h)

## Syntax

```c
bool SDL_EnumerateProperties(SDL_PropertiesID props, SDL_EnumeratePropertiesCallback callback, void *userdata);
```

## Function Parameters

|                                                                    |              |                                         |
| ------------------------------------------------------------------ | ------------ | --------------------------------------- |
| [SDL_PropertiesID](SDL_PropertiesID)                               | **props**    | the properties to query.                |
| [SDL_EnumeratePropertiesCallback](SDL_EnumeratePropertiesCallback) | **callback** | the function to call for each property. |
| void *                                                             | **userdata** | a pointer that is passed to `callback`. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The callback function is called for each property in the group of
properties. The properties are locked during enumeration.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## Code Examples

```c
// Example program
// Use SDL3 to enumerate the display properties of every display

#include <SDL3/SDL_log.h>
#include <SDL3/SDL_main.h>
#include <SDL3/SDL_video.h>


static void
my_enumerate_properties_callback(void *userdata, SDL_PropertiesID props, const char *name)
{
  SDL_PropertyType prop_type = SDL_GetPropertyType(props, name);

  switch (prop_type) {
    case SDL_PROPERTY_TYPE_POINTER:
      SDL_Log("%s is a pointer poperty", name);
      break;
    case SDL_PROPERTY_TYPE_STRING:
      SDL_Log(
        "%s is a string property with value %s", name, SDL_GetStringProperty(props, name, ""));
      break;
    case SDL_PROPERTY_TYPE_NUMBER:
      SDL_Log("%s is a number property with value %"SDL_PRIs64, name, SDL_GetNumberProperty(props, name, 0));
      break;
    case SDL_PROPERTY_TYPE_FLOAT:
      SDL_Log("%s is a float property with value %f", name, SDL_GetFloatProperty(props, name, 0.0f));
      break;
    case SDL_PROPERTY_TYPE_BOOLEAN:
      SDL_Log(
        "%s is a boolean property with value %d", name, SDL_GetBooleanProperty(props, name, false));
      break;
    case SDL_PROPERTY_TYPE_INVALID:
    default:
      SDL_Log("%s is an invalid property", name);
      break;
  }
}


int
main(int argc, char** argv)
{
  if (!SDL_Init(SDL_INIT_VIDEO)) {
    SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
    return 0;
  }

  SDL_Log("SDL initialized");

  int num_displays;
  SDL_DisplayID *displays = SDL_GetDisplays(&num_displays);
  SDL_Log("Found %d displays.", num_displays);

  for(int i = 0; i < num_displays; i++) {
    SDL_PropertiesID prop_id = SDL_GetDisplayProperties(displays[i]);
    SDL_Log("Display %d has properties ID %d", i, prop_id);

    if(!SDL_EnumerateProperties(prop_id, my_enumerate_properties_callback, NULL)) {
      SDL_Log("Error enumerating properties: %s.", SDL_GetError());
    }
  }

  SDL_free(displays);

  return 0;
}
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProperties](CategoryProperties)

