#include "brainParts/Brain.h"

Brain::Brain() { printf("Hello from brain \n"); }

void Brain::Hello() {
  printf("Hello\n");
  neuronMap.insert(std::make_pair<unsigned long, Neuron *>(1, new Neuron()));
}

Neuron *Brain::getNeuron(unsigned long nID) { return neuronMap[nID]; }
Neuron *Brain::createNeuron(unsigned long neuronID) {
  // Neuron *neuronTmp = new Neuron();
  neuronMap.insert(std::make_pair<unsigned long, Neuron *>(neuronID, new Neuron()));
  return neuronMap[1];
}

#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests written here, to test impl. details") {
  CHECK(true);
}
#endif
