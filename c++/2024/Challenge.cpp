#include "Challenge.hpp"

#include <cstdlib>
#include <fstream>
#include <sstream>

using namespace aoc;

Challenge::Challenge(const std::string_view& relativeInputFilePath) {

    char* aocTop;
    size_t bytesWritten;
    _dupenv_s(&aocTop, &bytesWritten, std::string{ AOC_TOP_ENV }.c_str());

	if (!aocTop) {
		std::ostringstream errMsg;
		errMsg << AOC_TOP_ENV << " is not set in the environment. Did you source?";
		throw std::runtime_error{errMsg.str()};
	}

	std::ostringstream fullFilePath;
	fullFilePath << std::string{aocTop} << "\\" << relativeInputFilePath;

	inputFilePath = fullFilePath.str();
    challengeInput = loadChallengeInput(inputFilePath);

    delete aocTop;

}

challenge_input_t Challenge::loadChallengeInput(const std::string_view& inputFilePath) {

    std::ifstream inputFile{ std::string{inputFilePath} };

    if (!inputFile) {
        std::ostringstream errMsg;
        errMsg << "Unable to read challenge input file: " << inputFilePath << ". Did you source?";
        throw std::ios_base::failure{ errMsg.str() };
    }

    challenge_input_t fileLines;
    std::string nextLine;

    while (std::getline(inputFile, nextLine)) {
        fileLines.push_back(nextLine);
    }

    return fileLines;

}