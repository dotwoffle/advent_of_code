#include "day1.hpp"

#include "Challenge.hpp"

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <set>
#include <sstream>
#include <utility>

using namespace aoc;

Day1Challenge::Day1Challenge() : Challenge{ "inputs\\2024\\day1.txt" }, LOCATION_LISTS{ buildLocationLists(challengeInput) } {}

Day1Challenge::location_lists_t Day1Challenge::buildLocationLists(const challenge_input_t& challengeInput) {

	location_lists_t locationLists;

	for (const std::string& line : challengeInput) {

		std::istringstream lineStream{ line };
		size_t entry1, entry2;

		lineStream >> entry1 >> entry2;

		locationLists.first.push_back(entry1);
		locationLists.second.push_back(entry2);

	}

	return locationLists;

}

size_t Day1Challenge::challengePart1() const noexcept {
	
	location_lists_t locationListsCopy{ LOCATION_LISTS };
	size_t sum{ 0 };

	std::sort(locationListsCopy.first.begin(), locationListsCopy.first.end());
	std::sort(locationListsCopy.second.begin(), locationListsCopy.second.end());

	for (size_t i = 0; i < locationListsCopy.first.size(); i++) {
		sum += std::labs(locationListsCopy.first[i] - locationListsCopy.second[i]);
	}

	return sum;

}

size_t Day1Challenge::challengePart2() const noexcept {
	
	std::set<size_t> uniqueFromFirstList;
	size_t sum{ 0 };

	for (size_t entry : LOCATION_LISTS.first) {
		uniqueFromFirstList.insert(entry);
	}

	for (size_t entry : uniqueFromFirstList) {
		sum += entry * std::count(LOCATION_LISTS.second.begin(), LOCATION_LISTS.second.end(), entry);
	}

	return sum;

}