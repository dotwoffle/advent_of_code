#include "day1.hpp"

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <set>
#include <sstream>
#include <utility>

using location_lists_t = std::pair<std::vector<size_t>, std::vector<size_t>>;

location_lists_t buildLocationLists(const std::vector<std::string>& challengeInput) {
	
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

size_t challengePart1(const std::vector<std::string>& challengeInput) {
	
	auto locationLists{ buildLocationLists(challengeInput) };
	size_t sum{ 0 };

	std::sort(locationLists.first.begin(), locationLists.first.end());
	std::sort(locationLists.second.begin(), locationLists.second.end());

	for (size_t i = 0; i < locationLists.first.size(); i++) {
		sum += std::labs(locationLists.first[i] - locationLists.second[i]);
	}

	return sum;

}

size_t challengePart2(const std::vector<std::string>& challengeInput) {
	
	auto locationLists{ buildLocationLists(challengeInput) };
	std::set<size_t> uniqueFromFirstList;
	size_t sum{ 0 };

	for (size_t entry : locationLists.first) {
		uniqueFromFirstList.insert(entry);
	}

	for (size_t entry : uniqueFromFirstList) {
		sum += entry * std::count(locationLists.second.begin(), locationLists.second.end(), entry);
	}

	return sum;

}
