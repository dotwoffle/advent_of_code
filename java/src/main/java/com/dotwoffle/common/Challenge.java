package com.dotwoffle.common;

public abstract class Challenge {

    public final int YEAR;
    public final int DAY;

    public void run() {
        System.out.println("Running challenge (" + YEAR + " day " + DAY + ")");
    }

    protected Challenge(int year, int day) {

        this.YEAR = year;
        this.DAY = day;

        ChallengeFactory.registerChallenge(year, day, this.getClass());

    }

    protected abstract int runPart1();
    protected abstract int runPart2();

}
