#pragma once

#include "brainParts/Neuron.h"
/**
 * This is a dummy class to demonstrate features of the boiler plate.
 */
class BIMB {
	public:

  /**
   * Default constructor for Dummy (does nothing).
   */
  BIMB();
  int main();
};


#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests in headers if we want")
{
//    BIMB d;
//    CHECK(d.doSomething() == true);
}
#endif
