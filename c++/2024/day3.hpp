#pragma once

#include "Challenge.hpp"

#include <concepts>
#include <vector>

namespace aoc {

class Day3Challenge : public Challenge {

public:

	Day3Challenge();

	size_t challengePart1() const noexcept override;

	size_t challengePart2() const noexcept override;

};

}