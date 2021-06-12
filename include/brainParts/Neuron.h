#pragma once
#include <cstdio>

/**
 * Neuron for the brain
 */
class Neuron {
	public:

  /**
   * Default constructor for Dummy (does nothing).
   */
  Neuron();
  /**
   * Returns a bool.
   * @return Always True.
   */
  bool printHello();
};


#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests in headers if we want")
{
    Neuron d;
    CHECK(d.printHello() == true);
}
#endif
