#pragma once

#include "Challenge.hpp"

#include <string>
#include <string_view>
#include <vector>

namespace aoc {

class Day1Challenge : public Challenge {

public:

	Day1Challenge();

	size_t challengePart1() const noexcept override;

	size_t challengePart2() const noexcept override;

private:

	using location_lists_t = std::pair<std::vector<size_t>, std::vector<size_t>>;

	const location_lists_t LOCATION_LISTS;

	static location_lists_t buildLocationLists(const challenge_input_t &challengeInput);

};

}