#include "day2.hpp"

#include <fstream>
#include <ios>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

static std::vector<std::string> loadChallengeInput() {
    
    std::ifstream inputFile{std::string{INPUT_FILE_PATH}};

    if(!inputFile) {
        std::ostringstream errMsg;
        errMsg << "Unable to read challenge input file: " << INPUT_FILE_PATH << ". Did you source?";
        throw std::ios_base::failure{errMsg.str()};
    }

    std::vector<std::string> fileLines;
    std::string nextLine;

    while(std::getline(inputFile, nextLine)) {
        fileLines.push_back(nextLine);
    }

    return fileLines;

}

int main() {
    
    const auto challengeInput = loadChallengeInput();

    std::cout << "Starting challenge" << std::endl;
    std::cout << "-------------- PART 1 --------------" << std::endl;
    std::cout << challengePart1(challengeInput) << std::endl;
    std::cout << "-------------- PART 2 --------------" << std::endl;
    std::cout << challengePart2(challengeInput) << std::endl;
    std::cout << "--------------- DONE ---------------" << std::endl;

}