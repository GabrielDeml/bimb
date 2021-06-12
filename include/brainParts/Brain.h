#pragma once
#include "brainParts/Neuron.h"
#include <cstdio>
#include <map>
class Brain {
private:
  std::map<unsigned long, Neuron*> neuronMap;
  unsigned long neuronID = 0;

public:
  /**
   * Default constructor for Brain.
   */
  Brain();
  void Hello();
  Neuron *getNeuron(unsigned long neuronID);
  Neuron *createNeuron();
};

#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests in headers if we want") {}
#endif
