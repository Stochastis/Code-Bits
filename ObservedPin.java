import java.util.ArrayList;
import java.util.List;

public class ObservedPin {

    static int[][] numberGroups = { { 0, 8 }, { 1, 2, 4 }, { 1, 2, 3, 5 }, { 2, 3, 6 }, { 1, 4, 5, 7 },
            { 2, 4, 5, 6, 8 },
            { 3, 5, 6, 9 }, { 4, 7, 8 }, { 0, 5, 7, 8, 9 }, { 6, 8, 9 } };

    // Go through all possible combinations of the numbers and add them to the
    // result list.
    public static List<String> recursion(int charIndex, String pin, List<String> result) {
        System.out.println("Inside recursion");
        if (charIndex == pin.length()) {
            result.add(pin);
            return result;
        }
        for (int i = 0; i < numberGroups[Character.getNumericValue(pin.charAt(charIndex))].length; i++) {
            String currentPin = pin.substring(0, charIndex)
                    + numberGroups[Character.getNumericValue(pin.charAt(charIndex))][i]
                    + pin.substring(charIndex + 1);
            result = recursion(charIndex + 1, currentPin, result);
        }
        return result;
    }

    public static List<String> getPINs(String observed) {
        System.out.println("Inside getPINs");
        List<String> finalResult = recursion(0, observed, new ArrayList<String>());

        return finalResult;
    }

    // Main method
    public static void main(String[] args) {
        System.out.println("Running getPINs");
        System.out.println(getPINs("369"));
    }

}