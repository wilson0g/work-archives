import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Collections;
import java.util.ArrayList;
public class FootballRanks {

    public static void goalranks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 = ballerz[m];
                Player baller2 = ballerz[m+1];
                if (baller1.getGoals()<baller2.getGoals()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }
            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer = ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getGoals());
        }

        String filePath = "GoldenBoot.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer =  ballerz [i];
            content = content + futballer.getName()+ "-" + futballer.getGoals()+ " Goals\n";
            System.out.println();
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Golden Boot list completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to Sfile: " + e.getMessage());
        }



    }


    public static void assistranks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 = ballerz[m];
                Player baller2 = ballerz[m+1];
                if (baller1.getAssists()<baller2.getAssists()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer =  ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getAssists());
        }

        String filePath = "AssistsRanks.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer = ballerz [i];
            content = content + futballer.getName()+ "-" + futballer.getAssists()+ " Assists\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Assists Ranking list completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }



    }

    public static void tacklesRanks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 = ballerz[m];
                Player baller2 =  ballerz[m+1];
                if (baller1.getTackles()<baller2.getTackles()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer = ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getTackles());
        }

        String filePath = "TacklesRanks.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer =  ballerz [i];
            content = content + futballer.getName()+ "-" + futballer.getTackles()+ " Tackles\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Tackles Ranking list completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }



    }

    public static void YellowCardsRanks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 =  ballerz[m];
                Player baller2 =  ballerz[m+1];
                if (baller1.getYellowCard()<baller2.getYellowCard()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer =  ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getYellowCard());
        }

        String filePath = "YellowCardRanks.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer = ballerz [i];
            content = content + futballer.getName()+ "-" + futballer.getYellowCard()+ " Yellow Cards\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Yellow Card Ranking list completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

    }

    public static void redCardsRanks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 = ballerz[m];
                Player baller2 = ballerz[m+1];
                if (baller1.getRedCard()<baller2.getRedCard()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer =  ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getRedCard());
        }

        String filePath = "RedCardsRanks.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer = ballerz [i];
            content =  content + futballer.getName()+ "-" + futballer.getRedCard()+ " Red Cards\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Red Card Ranking list completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }


    }

    public static void passesCompletedRanks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 = ballerz[m];
                Player baller2 = ballerz[m+1];
                if (baller1.getPassesCompleted()<baller2.getPassesCompleted()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer = ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getPassesCompleted());
        }
        String filePath = "PassesCompletedRanks.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer = ballerz [i];
            content = content + futballer.getName()+ "-" + futballer.getPassesCompleted()+ " Passes Completed\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Passes Completed Ranking list completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

    }

    public static void SavesRanks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 =  ballerz[m];
                Player baller2 =  ballerz[m+1];
                if (baller1.getSaves()<baller2.getSaves()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer =  ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getSaves());
        }

        String filePath = "SavesRanks.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer =  ballerz [i];
            content = content + futballer.getName()+ "-" + futballer.getSaves()+ " Saves\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Saves Ranking List completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

    }

    public static void cleanSheetRanks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 =  ballerz[m];
                Player baller2 =  ballerz[m+1];
                if (baller1.getCleansheets()<baller2.getCleansheets()) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer =  ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getCleansheets());
        }
        String filePath = "GoldenGloves.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer = ballerz [i];
            content = content + futballer.getName()+ "-" + futballer.getCleansheets()+ " Cleansheet\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Golden gloves list completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }

    }

    public static void overallRanks(ArrayList<Player> myPlayer){
        Player[] ballerz = new Player[myPlayer.size()];
        myPlayer.toArray(ballerz);
        for (int i=0; i<ballerz.length-1;i++){
            for (int m =0; m<ballerz.length-1-i; m++){
                Player baller1 =  ballerz[m];
                Player baller2 = ballerz[m+1];
                int weightedSum1 = (baller1.getAssists()*10) + (baller1.getGoals()*5);
                int weightedSum2 = (baller2.getAssists()*10) + (baller2.getGoals()*5);
                if (weightedSum1<weightedSum2) {
                    Player temp = ballerz[m];
                    ballerz[m] = ballerz[m + 1];
                    ballerz[m + 1] = temp;
                }


            }
        }
        for (int i =0; i<ballerz.length; i++){
            Player futballer = ballerz[i];
            System.out.println(futballer.getName() + "-" + futballer.getAssists()*10 + futballer.getGoals()*5);
        }
        String filePath = "OverallBestPlayer.txt";
        String content = "";

        for (int i = 0; i< ballerz.length; i++){
            Player futballer = ballerz [i];
            content = content + futballer.getName()+ "-" +  (futballer.getAssists()*10 + futballer.getGoals()*5)+"\n";
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            writer.write(content);
            writer.newLine(); // Adds a new line
            writer.write("Overall Best Player List completed!");
            System.out.println("File written successfully: " + filePath);
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }



    }


}
