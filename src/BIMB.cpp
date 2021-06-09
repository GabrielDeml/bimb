#include "BIMB.h"
#include "brainParts/Brain.h"
#include "brainParts/Neuron.h"

BIMB::BIMB() {
  Neuron neuron = Neuron();
  neuron.printHello();
}

int BIMB::main() {
  Brain brain = Brain();
  brain.Hello();
  return 0;
}

#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests written here, to test impl. details") {
  CHECK(true);
}
#endif
