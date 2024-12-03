#include "Challenge.hpp"
#include "day1.hpp"

#include <iostream>
#include <memory>

int main() {

    
    std::unique_ptr<aoc::Challenge> challenge;

    try {
        challenge = std::make_unique<aoc::Day1Challenge>();
    }
    catch (const std::exception& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    std::cout << "Starting challenge" << std::endl;
    std::cout << "-------------- PART 1 --------------" << std::endl;
    std::cout << challenge->challengePart1() << std::endl;
    std::cout << "-------------- PART 2 --------------" << std::endl;
    std::cout << challenge->challengePart2() << std::endl;
    std::cout << "--------------- DONE ---------------" << std::endl;

}