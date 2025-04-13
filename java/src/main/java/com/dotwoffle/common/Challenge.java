package com.dotwoffle.common;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.nio.file.Path;
import java.util.List;
import java.util.stream.Collectors;

public abstract class Challenge {

    public final int YEAR;
    public final int DAY;

    public void run() throws FileNotFoundException {

        loadChallengeInput();

        System.out.println("---------- CHALLENGE PART 1 ----------");
        System.out.println(runPart1());
        System.out.println("---------- CHALLENGE PART 2 ----------");
        System.out.println(runPart2());

    }

    protected List<String> challengeInput;

    protected Challenge() {

        ChallengeClass anno = this.getClass().getAnnotation(ChallengeClass.class);

        if(anno == null) {
            throw new IllegalStateException("Class inherited from " + this.getClass().getName() + " but did not tag itself with " + ChallengeClass.class.getName() + " annotation");
        }

        this.YEAR = anno.year();
        this.DAY = anno.day();

    }

    protected abstract int runPart1();
    protected abstract int runPart2();

    private static final Path CHALLENGE_INPUTS_BASE_PATH = Path.of("C:\\Users\\loren\\code\\advent_of_code\\inputs");

    private void loadChallengeInput() throws FileNotFoundException {

        Path challengeInputPath = CHALLENGE_INPUTS_BASE_PATH
                .resolve(Integer.toString(YEAR))
                .resolve("day" + DAY + ".txt");
        BufferedReader inputFileReader = new BufferedReader(new FileReader(challengeInputPath.toFile()));

        challengeInput = inputFileReader.lines().collect(Collectors.toList());

    }

}
