#include "day2.hpp"

#include <cmath>
#include <iterator>
#include <limits>
#include <sstream>

using namespace aoc;

Day2Challenge::Day2Challenge() : Challenge{ "inputs\\2024\\day2.txt" }, REPORTS{loadReports(challengeInput)} {}

size_t Day2Challenge::challengePart1() const noexcept {
	return countSafeReports(REPORTS, isReportSafe);
}

size_t Day2Challenge::challengePart2() const noexcept {

	auto checkIfReportIsSafe = [](const std::vector<size_t>& report) {

		if (isReportSafe(report)) {
			return true;
		}

		for (const auto& subReport : enumeratePossibleReports(report)) {
			if (isReportSafe(subReport)) {
				return true;
			}
		}

		return false;

	};

	return countSafeReports(REPORTS, checkIfReportIsSafe);

}

Day2Challenge::reports_t Day2Challenge::loadReports(const challenge_input_t& challengeInput)
{
	reports_t reports;
	
	for (const auto& line : challengeInput) {
		
		std::vector<size_t> report;
		std::istringstream reportStream{ line };
		size_t entry;

		while (!reportStream.eof()) {
			reportStream >> entry;
			report.push_back(entry);
		}

		reports.push_back(report);

	}

	return reports;

}

bool Day2Challenge::isReportSafe(const std::vector<size_t>& report) {

	int previousDistance = std::numeric_limits<int>::max();

	for (size_t i = 0; i < report.size() - 1; i++) {

		int distance = report[i] - report[i + 1];

		if (std::abs(distance) < 1 || std::abs(distance) > 3) {
			return false;
		}

		if (previousDistance != std::numeric_limits<int>::max() && (previousDistance < 0 != distance < 0)) {
			return false;
		}

		previousDistance = distance;

	}

	return true;

}

Day2Challenge::reports_t Day2Challenge::enumeratePossibleReports(const std::vector<size_t>& report)
{

	reports_t reports;

	for (size_t i = 0; i < report.size(); i++) {

		std::vector<size_t> newReport;

		for (int j = 0; j < report.size(); j++) {
			if (i != j) {
				newReport.push_back(report[j]);
			}
		}

		reports.push_back(newReport);

	}

	return reports;
}
