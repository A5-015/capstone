cmake_minimum_required(VERSION 3.5)
project(ramen)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_EXPORT_COMPILE_COMMANDS True)
# -Wall -Wextra -Woverflow
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -pthread -Werror --coverage -O0")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS}")

add_definitions(-D _RAMEN_UNIT_TESTING_)

file(GLOB TESTFILES test/test_*.cpp)

# Target ramen_unit_tests
add_executable(ramen_unit_tests test/main.cpp "${PROJECT_BINARY_DIR}/test/include/fake_serial.cpp"
                                    "${PROJECT_BINARY_DIR}/test/include/scheduler.cpp"
                                    "${PROJECT_BINARY_DIR}/src/ramen/utils.cpp"
                                    "${PROJECT_BINARY_DIR}/src/ramen/message.cpp"
                                    "${PROJECT_BINARY_DIR}/src/ramen/mesh_network.cpp"
                                    "${PROJECT_BINARY_DIR}/src/ramen/logger.hpp"
                                    "${PROJECT_BINARY_DIR}/src/ramen/data_queue.cpp"
                                    "${PROJECT_BINARY_DIR}/src/ramen/log_holder.cpp"
                                    "${PROJECT_BINARY_DIR}/src/ramen/server.cpp"
                                    ${TESTFILES})

target_include_directories(ramen_unit_tests PUBLIC "${PROJECT_BINARY_DIR}/src/"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/"
                                                  "${PROJECT_BINARY_DIR}/test/"
                                                  "${PROJECT_BINARY_DIR}/test/include/"
                                                  "${PROJECT_BINARY_DIR}/test/TaskScheduler/src/"
                                                  "${PROJECT_BINARY_DIR}/test/ArduinoJson/src/")

# Target virtual_esp
add_executable(virtual_esp test/virtual_esp.cpp "${PROJECT_BINARY_DIR}/test/include/fake_serial.cpp"
                                                  "${PROJECT_BINARY_DIR}/test/include/scheduler.cpp"
                                                  "${PROJECT_BINARY_DIR}/test/include/cxxopts.hpp"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/utils.cpp"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/message.cpp"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/mesh_network.cpp"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/logger.hpp"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/data_queue.cpp"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/log_holder.cpp"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/server.cpp")

target_include_directories(virtual_esp PUBLIC "${PROJECT_BINARY_DIR}/src/"
                                                  "${PROJECT_BINARY_DIR}/src/ramen/"
                                                  "${PROJECT_BINARY_DIR}/test/"
                                                  "${PROJECT_BINARY_DIR}/test/include/"
                                                  "${PROJECT_BINARY_DIR}/test/TaskScheduler/src/"
                                                  "${PROJECT_BINARY_DIR}/test/ArduinoJson/src/")