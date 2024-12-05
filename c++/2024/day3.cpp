#include "day3.hpp"

#include <iostream>
#include <regex>

using namespace aoc;

Day3Challenge::Day3Challenge() : Challenge{ "inputs\\2024\\day3.txt" } {}

size_t Day3Challenge::challengePart1() const noexcept {

	const std::regex mulRegex{ "mul\\(\\d*,\\d*\\)" };
	size_t sum{ 0 };

	for (const auto& line : challengeInput) {
		for (std::sregex_iterator iter = std::sregex_iterator(line.begin(), line.end(), mulRegex); iter != std::sregex_iterator{}; iter++) {
			
			const std::string matchedString{ (*iter).str() };
			const std::string firstNum = matchedString.substr(
					matchedString.find_first_of("(") + 1,
					matchedString.find_first_of(",")
			);
			const std::string lastNum = matchedString.substr(
					matchedString.find_first_of(",") + 1,
					matchedString.find_first_of(")")
			);

			sum += std::stoi(firstNum) * std::stoi(lastNum);

		}
	}

	return sum;

}

size_t Day3Challenge::challengePart2() const noexcept {

	const std::regex instructionRegex{ "(mul\\(\\d*,\\d*\\))|(do\\(\\))|(don't\\(\\))" };
	size_t sum{ 0 };
	bool mulsEnabled = true;

	for (const auto& line : challengeInput) {

		for (std::sregex_iterator iter = std::sregex_iterator(line.begin(), line.end(), instructionRegex); iter != std::sregex_iterator{}; iter++) {

			const std::string matchedString{ (*iter).str() };

			if (matchedString.starts_with("don't")) {
				mulsEnabled = false;
			}
			else if (matchedString.starts_with("do")) {
				mulsEnabled = true;
			}
			else if(mulsEnabled) {

				const std::string firstNum = matchedString.substr(
					matchedString.find_first_of("(") + 1,
					matchedString.find_first_of(",")
				);
				const std::string lastNum = matchedString.substr(
					matchedString.find_first_of(",") + 1,
					matchedString.find_first_of(")")
				);

				sum += std::stoi(firstNum) * std::stoi(lastNum);

			}

		}

	}

	return sum;

}