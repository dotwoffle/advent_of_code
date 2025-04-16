package com.dotwoffle.common;

import org.reflections.Reflections;
import org.reflections.scanners.Scanners;

import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;

public class ChallengeFactory {

    public static void registerChallenges(String packageName) {

        Reflections r = new Reflections(packageName);
        Set<Class<?>> annotatedChallengeClasses = r.get(Scanners.TypesAnnotated.with(ChallengeClass.class).asClass())
                .stream()
                .filter(Challenge.class::isAssignableFrom)
                .collect(Collectors.toSet());

        for(Class<?> c : annotatedChallengeClasses) {

            Class<? extends Challenge> challengeClass = c.asSubclass(Challenge.class);
            ChallengeClass anno = challengeClass.getAnnotation(ChallengeClass.class);

            CHALLENGE_REGISTRY.put(new ChallengeKey(anno.year(), anno.day()), challengeClass);

        }

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

        @Override
        public boolean equals(Object obj) {

            if(obj instanceof ChallengeKey k) {
                return this.YEAR == k.YEAR && this.DAY == k.DAY;
            }

            return false;

        }

        @Override
        public int hashCode() {
            return Objects.hash(YEAR, DAY);
        }

    }
    private static final Map<ChallengeKey, Class<? extends Challenge>> CHALLENGE_REGISTRY = new HashMap<>();

}