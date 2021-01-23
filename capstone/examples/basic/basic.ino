#include "Arduino.h"
#include "ramen.h"

#define MESH_NAME "ramen"
#define MESH_PASSWORD "ramen123*"
#define MESH_PORT 5555

ramen::Server consensus_on_mesh;

void setup() {
  Serial.begin(115200);
  consensus_on_mesh.init(MESH_NAME, MESH_PASSWORD, MESH_PORT);
}

void loop() { consensus_on_mesh.update(); }