#pragma once

#include <string>
#include <vector>

namespace aoc {

using challenge_input_t = std::vector<std::string>;

namespace {
constexpr std::string_view AOC_TOP_ENV{ "AOC_TOP" };
}

class Challenge {

public:

	std::string inputFilePath;
    challenge_input_t challengeInput;

	Challenge(const std::string_view& relativeInputFilePath);

    static challenge_input_t loadChallengeInput(const std::string_view& inputFilePath);

	virtual size_t challengePart1() const noexcept = 0;

	virtual size_t challengePart2() const noexcept = 0;

};

}