//no one likes the .hpp extension
#include <iostream>

int main(){
    // No namespace here :(
    std::cout << "Hello i am an output" << /*Gets killed*/ std::endl;
    return 0; //Dead
}