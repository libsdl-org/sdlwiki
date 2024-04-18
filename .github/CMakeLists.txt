cmake_minimum_required(VERSION 3.20)
project(sdlwikipp LANGUAGES C CXX)

find_package(Python3 REQUIRED COMPONENTS Interpreter)

option(USE_FIND_PACKAGE "Use find_package to find SDL projects" ON)

set(SDLWIKI_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/.." CACHE PATH "Path to sdlwiki root source folder")
set(OUTPUT_ROOT "${CMAKE_CURRENT_BINARY_DIR}/wikidir" CACHE PATH "Path to generated wiki root foler")

set(EXAMPLE_DIR "${OUTPUT_ROOT}/examples")
file(MAKE_DIRECTORY "${EXAMPLE_DIR}")

get_filename_component(sdlwiki_root "${SDLWIKI_ROOT}" ABSOLUTE)

if(USE_FIND_PACKAGE)
  find_package(SDL2 REQUIRED)
  find_package(SDL2_image REQUIRED)
  find_package(SDL2_mixer REQUIRED)
  find_package(SDL2_net REQUIRED)
  find_package(SDL2_ttf REQUIRED)
  find_package(SDL2_rtf REQUIRED)
  find_package(SDL3 REQUIRED)
  find_package(SDL3_image REQUIRED)
  find_package(SDL3_mixer REQUIRED)
  find_package(SDL3_net REQUIRED)
  find_package(SDL3_ttf REQUIRED)
  find_package(SDL3_rtf REQUIRED)
  find_package(Vulkan REQUIRED)
endif()

find_package(JNI REQUIRED)

message(STATUS "sdlwiki root folder is ${sdlwiki_root}")
message(STATUS "output root folder is  ${OUTPUT_ROOT}")

find_program(PANDOC_BIN NAMES pandoc)
if(NOT PANDOC_BIN)
    message(FATAL_ERROR "Cannot find pandoc")
endif()

file(GLOB_RECURSE MARKDOWN_SOURCES "${sdlwiki_root}/*.md")
file(GLOB_RECURSE MEDIAWIKI_SOURCES "${sdlwiki_root}/*.mediawiki")

list(LENGTH MARKDOWN_SOURCES  nb_markdown_sources)
list(LENGTH MEDIAWIKI_SOURCES nb_mediawiki_sources)

message(STATUS "Found ${nb_markdown_sources} Markdown pages")
message(STATUS "Found ${nb_mediawiki_sources} MediaWiki pages")

enable_testing()

execute_process(
    COMMAND "${Python3_EXECUTABLE}" "${CMAKE_CURRENT_SOURCE_DIR}/extract_example.py"
        --outdir "${EXAMPLE_DIR}"
        --docroot "${sdlwiki_root}"
        ${MARKDOWN_SOURCES} ${MEDIAWIKI_SOURCES}
    RESULT_VARIABLE res
    OUTPUT_VARIABLE example_paths
    ERROR_VARIABLE err
)
if(NOT res EQUAL 0)
    message(WARNING "An error happened while extracting some example code:\n${err}")
endif()
string(STRIP "${example_paths}" example_paths)
list(LENGTH example_paths nb_example_paths)
message(STATUS "Found ${nb_example_paths} Example code blocks")

foreach(example_path IN LISTS example_paths)
    cmake_path(RELATIVE_PATH example_path BASE_DIRECTORY "${EXAMPLE_DIR}" OUTPUT_VARIABLE example_relative)
    string(MAKE_C_IDENTIFIER "${example_relative}" target)

    add_library(${target} OBJECT "${example_path}")
    target_compile_definitions(${target} PRIVATE __ANDROID__)
    target_link_libraries(${target} PRIVATE JNI::JNI)

    get_filename_component(example_relative_directory "${example_relative}" DIRECTORY)
    get_filename_component(sdl_project "${example_relative_directory}" NAME)
    if(USE_FIND_PACKAGE)
      target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/${sdl_project}/include")
      if(sdl_project MATCHES "^SDL2_rtf")
        target_link_libraries(${target} PRIVATE SDL2_ttf::SDL2_ttf)
      elseif(sdl_project MATCHES "^SDL3_ttf")
        target_link_libraries(${target} PRIVATE SDL3_ttf::SDL3_ttf)
      endif()
      if(sdl_project MATCHES "^SDL2")
        target_link_libraries(${target} PRIVATE SDL2::SDL2 Vulkan::Vulkan)
      elseif(sdl_project MATCHES "^SDL3")
        target_link_libraries(${target} PRIVATE SDL3::SDL3 Vulkan::Vulkan)
      endif()
    else()
      target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/${sdl_project}/include")
      if(sdl_project MATCHES "^SDL2_[rt]tf")
        target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/SDL2_ttf")
      elseif(sdl_project MATCHES "^SDL3_[rt]tf")
        target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/SDL3_ttf/include")
      endif()
      if(sdl_project MATCHES "^SDL2_rtf")
        target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/SDL2_rtf")
      elseif(sdl_project MATCHES "^SDL3_ttf")
        target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/SDL3_ttf/include")
      endif()
      if(sdl_project MATCHES "^SDL2")
        target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/SDL2/include/SDL2")
      elseif(sdl_project MATCHES "^SDL3")
        target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/SDL3/include")
        target_include_directories(${target} PRIVATE "${CMAKE_CURRENT_SOURCE_DIR}/../external/SDL3/src/video/khronos")
      endif()
    endif()

    add_test(
        NAME "${example_relative}-example"
        COMMAND "${CMAKE_COMMAND}" --build "${CMAKE_BINARY_DIR}" --target "${target}"
    )
    set_property(TEST "${example_relative}-example" PROPERTY TIMEOUT 10)
endforeach()

foreach(src IN LISTS MARKDOWN_SOURCES MEDIAWIKI_SOURCES)
    cmake_path(RELATIVE_PATH src BASE_DIRECTORY "${sdlwiki_root}" OUTPUT_VARIABLE src_relative)
    cmake_path(GET src_relative PARENT_PATH src_reldirectory)
    if(src_reldirectory AND NOT IS_DIRECTORY "${OUTPUT_ROOT}/${src_reldirectory}")
        execute_process(
            COMMAND "${CMAKE_COMMAND}" -E make_directory "${OUTPUT_ROOT}/${src_reldirectory}"
        )
    endif()

    if(src MATCHES "\\.mediawiki$")
        set(fmt "mediawiki")
    elseif(src MATCHES "\\.md$")
        set(fmt "gfm")  # GitHub-Flavored Markdown
    else()
        message(FATAL_ERROR "Unknown document type (${src})")
    endif()
    add_test(
        NAME "${src_relative}"
        COMMAND "${PANDOC_BIN}" --fail-if-warnings --verbose -f ${fmt} -t html -o "${OUTPUT_ROOT}/${src_relative}.html" "${src}"
    )
    set_property(TEST "${src_relative}" PROPERTY TIMEOUT 5)
endforeach()

