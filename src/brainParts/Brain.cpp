#include "brainParts/Brain.h"
#include <cstdio>

Brain::Brain() {
    printf("Hello from brain \n");
}

void Brain::Hello(){
    printf("Hello\n");
}

#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests written here, to test impl. details")
{
    CHECK(true);
}
#endif

