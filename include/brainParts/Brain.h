#pragma once
class Brain {
	public:

  /**
   * Default constructor for Brain.
   */
  Brain();
  void Hello();
};


#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests in headers if we want")
{
  
}
#endif

