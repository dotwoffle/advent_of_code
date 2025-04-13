package com.dotwoffle;

import com.dotwoffle.common.Challenge;
import com.dotwoffle.common.ChallengeFactory;

import java.io.FileNotFoundException;

public class ChallengeRunner {

    public static void main(String[] args) {

        int year = Integer.parseInt(args[0]);
        int day = Integer.parseInt(args[1]);
        Challenge challenge;

        try {
            challenge = ChallengeFactory.createChallenge(year, day);
        } catch (ReflectiveOperationException e) {
            throw new RuntimeException(e);
        }

        try {
            challenge.run();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

    }

}