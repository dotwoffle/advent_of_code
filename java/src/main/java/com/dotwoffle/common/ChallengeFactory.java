package com.dotwoffle.common;

import java.util.HashMap;
import java.util.Map;

public class ChallengeFactory {

    public static void registerChallenge(int year, int day, Class<? extends Challenge> challengeClass) {
        CHALLENGE_REGISTRY.put(new ChallengeKey(year, day), challengeClass);
    }

    public static Challenge createChallenge(int year, int day) throws ReflectiveOperationException {

        ChallengeKey key = new ChallengeKey(year, day);

        if(!CHALLENGE_REGISTRY.containsKey(key)) {
            throw new ClassNotFoundException("No challenge class registered for " + year + " day " + day);
        }

        return CHALLENGE_REGISTRY.get(key).getDeclaredConstructor().newInstance();

    }

    private static class ChallengeKey {

        ChallengeKey(int year, int day) {
            this.YEAR = year;
            this.DAY = day;
        }

        final int YEAR;
        final int DAY;

    }

    private static final Map<ChallengeKey, Class<? extends Challenge>> CHALLENGE_REGISTRY = new HashMap<>();

}