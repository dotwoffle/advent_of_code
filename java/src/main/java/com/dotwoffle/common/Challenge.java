package com.dotwoffle.common;

import com.electronwill.nightconfig.core.file.FileConfig;

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
        setup();

        System.out.println("---------- CHALLENGE PART 1 ----------");
        System.out.println(runPart1());

        setup();

        System.out.println("---------- CHALLENGE PART 2 ----------");
        System.out.println(runPart2());

    }

    protected Challenge() {

        ChallengeClass anno = this.getClass().getAnnotation(ChallengeClass.class);

        if(anno == null) {
            throw new IllegalStateException("Class inherited from " + this.getClass().getName() + " but did not tag itself with " + ChallengeClass.class.getName() + " annotation");
        }

        this.YEAR = anno.year();
        this.DAY = anno.day();

    }

    protected List<String> challengeInput;

    protected abstract int runPart1();
    protected abstract int runPart2();
    protected void setup() {}

    private static final Path CHALLENGE_INPUTS_BASE_PATH;

    static {
        FileConfig aocConfig = FileConfig.of("C:\\Users\\loren\\code\\advent_of_code\\java\\src\\main\\resources\\config.toml");
        aocConfig.load();
        CHALLENGE_INPUTS_BASE_PATH = Path.of(aocConfig.<String>get("challengeInputsBasePath"));
        aocConfig.close();
    }

    private void loadChallengeInput() throws FileNotFoundException {

        Path challengeInputPath = CHALLENGE_INPUTS_BASE_PATH
                .resolve(Integer.toString(YEAR))
                .resolve("day" + DAY + ".txt");
        BufferedReader inputFileReader = new BufferedReader(new FileReader(challengeInputPath.toFile()));

        challengeInput = inputFileReader.lines().collect(Collectors.toList());

    }

}
