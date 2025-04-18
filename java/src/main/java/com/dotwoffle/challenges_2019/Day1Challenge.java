package com.dotwoffle.challenges_2019;

import com.dotwoffle.common.Challenge;
import com.dotwoffle.common.ChallengeClass;

import java.util.ArrayList;
import java.util.List;

@ChallengeClass(year=2019, day=1)
public class Day1Challenge extends Challenge {

    @Override
    protected void challengeSetup() {
        for(String line : challengeInput) {
            MODULE_MASSES.add(Integer.parseInt(line));
        }
    }

    @Override
    protected int runPart1() {

        int totalFuelRequirements = 0;

        for(int mass : MODULE_MASSES) {
            totalFuelRequirements += (mass / 3) - 2;
        }

        return totalFuelRequirements;

    }

    @Override
    protected int runPart2() {

        int totalFuelRequirements = 0;

        for(int mass : MODULE_MASSES) {
            totalFuelRequirements += calculateRecursiveFuelRequirements(mass);
        }

        return totalFuelRequirements;

    }

    private final List<Integer> MODULE_MASSES = new ArrayList<>();

    private static int calculateRecursiveFuelRequirements(int initialMass) {

        int fuelRequirement = (initialMass / 3) - 2;

        if(fuelRequirement <= 0) {
            return 0;
        }
        else {
            return fuelRequirement + calculateRecursiveFuelRequirements(fuelRequirement);
        }

    }

}
