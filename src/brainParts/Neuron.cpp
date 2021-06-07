#include "brainParts/Neuron.h"

Neuron::Neuron() {

}

bool Neuron::printHello(){
    printf("Hello");
    return true;
}




#ifdef ENABLE_DOCTEST_IN_LIBRARY
#include "doctest.h"
TEST_CASE("we can have tests written here, to test impl. details")
{
    CHECK(true);
}
#endif
