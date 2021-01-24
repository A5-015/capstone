#define CATCH_CONFIG_MAIN

#include <Arduino.h>

#include "catch2/catch.hpp"
#include "ramen/logger.hpp"

using namespace ramen::logger;
Logger Log;

SCENARIO("Logging test") {
  Log.setLogLevel(ERROR);
  Log(ERROR,
      "This message should be visible and there shouldn't be a debug message "
      "below\n");
  Log(DEBUG, "This message should NOT be visible\n");
  Log(ERROR,
      "This message should also be visible and a CRITICAL message should be "
      "visible below\n");
  Log(CRITICAL, "This message should be visible\n");
}