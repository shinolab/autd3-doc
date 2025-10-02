cmake_minimum_required(VERSION 3.21)

project(autd3-sample)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(${CMAKE_VERSION} VERSION_GREATER_EQUAL "3.24.0") 
  cmake_policy(SET CMP0135 NEW)
endif()

include(FetchContent)
if(WIN32)
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v36.0.2/autd3-v36.0.2-win-x64.zip
  )
elseif(APPLE)
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v36.0.2/autd3-v36.0.2-macos-aarch64.tar.gz
  )
else()
  FetchContent_Declare(
    autd3
    URL https://github.com/shinolab/autd3-cpp/releases/download/v36.0.2/autd3-v36.0.2-linux-x64.tar.gz
  )
endif()
set(USE_SYSTEM_EIGEN OFF)
FetchContent_MakeAvailable(autd3)

add_executable(main main.cpp)

target_link_libraries(main PRIVATE autd3::autd3 autd3::link::ethercrab)