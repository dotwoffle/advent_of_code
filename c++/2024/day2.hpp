#pragma once

#include "Challenge.hpp"

#include <concepts>
#include <vector>

namespace aoc {

class Day2Challenge : public Challenge {

public:

	Day2Challenge();

	size_t challengePart1() const noexcept override;

	size_t challengePart2() const noexcept override;

private:

	using reports_t = std::vector<std::vector<size_t>>;

	const reports_t REPORTS;

	static reports_t loadReports(const challenge_input_t& challengeInput);

	static bool isReportSafe(const std::vector<size_t>& report);

	static reports_t enumeratePossibleReports(const std::vector<size_t>& report);

	template <std::predicate<std::vector<size_t>> Predicate>
	static size_t countSafeReports(const reports_t &reports, const Predicate &validator) {
		
		size_t sum{ 0 };

		for (const auto& report : reports) {
			sum += validator(report) ? 1 : 0;
		}

		return sum;

	}

};

}