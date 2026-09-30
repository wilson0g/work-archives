import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;
public class WordCupMain {
    public static void main (String[] args){
        Scanner wilson = new Scanner(System.in);
        ArrayList<Player> futballerz = new ArrayList<>();
        System.out.println();
        System.out.println("1. Register World Cup Player");
        System.out.println("2. Update Player Metrics ");
        System.out.println("3. View Rankings");
        System.out.println("4. Exit");
        System.out.println();
        System.out.println();


        int menu = wilson.nextInt();
        wilson.nextLine();
        while (menu >0 && menu<5){
            if (menu ==1){
                //add player
                System.out.println("Please enter player's name:");
                String name = wilson.nextLine();
                while(name.isEmpty()){
                    System.out.println("Please enter player's name:");
                    name = wilson.nextLine();
                }
                System.out.println();

                System.out.println("Please enter player's club:");
                String yourClub = wilson.nextLine();
                while(yourClub.isEmpty()){
                    System.out.println("Please enter player's Club:");
                    yourClub = wilson.nextLine();
                }
                System.out.println();

                System.out.println("Please enter player's Country:");
                String yourNationality = wilson.nextLine();
                while(yourNationality.isEmpty()){
                    System.out.println("Please enter the player's Country:");
                    yourNationality = wilson.nextLine();
                }
                System.out.println();

                System.out.println("Please enter player's position:");
                String yourPosition = wilson.nextLine();
                while(yourPosition.isEmpty()){
                    System.out.println("Please enter player's position:");
                    yourPosition = wilson.nextLine();
                }
                System.out.println();

                System.out.println("Please enter player's FIFAID:");
                String yourFIFAID = wilson.nextLine();
                while(yourFIFAID.isEmpty()){
                    System.out.println("Please enter player's FIFAID:");
                    yourFIFAID = wilson.nextLine();
                }
                System.out.println();

                Player numberX;
                if(yourPosition.toLowerCase().equals("forward")){
                     numberX= new Offensivestats(name, yourClub, yourNationality, yourFIFAID, yourPosition);
                }
                else if(yourPosition.toLowerCase().equals("midfielder")){
                     numberX= new Generalstats(name, yourClub, yourNationality, yourFIFAID, yourPosition);
                }
                else if(yourPosition.toLowerCase().equals("defender")){
                     numberX= new Defensivestats(name, yourClub, yourNationality, yourFIFAID, yourPosition);
                }
                else{
                     numberX= new Keeperstats(name, yourClub, yourNationality, yourFIFAID, yourPosition);
                }
                futballerz.add(numberX);

                String filePath = "RegisteredWorldCupPlayers.txt";
                String content = "";

                content = content + "Name: " +name + "     Club: " + yourClub + "     Country: " +yourNationality+ "     Position: "+ yourPosition+ "     FIFA-ID: " +yourFIFAID + "\n";

                try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath, true))) {
                    writer.write(content);
                    writer.newLine(); // Adds a new line

                    //writer.write("Register World Cup Players completed!");
                    System.out.println("File written successfully: " + filePath);
                } catch (IOException e) {
                    System.err.println("Error writing to file: " + e.getMessage());
                }
                System.out.println();
                System.out.println();






            }
            else if (menu == 2) {
                int metric;
                String fifaID;
                int update;
                System.out.println("Which Metric are you updating?");
                System.out.println("1. Goals");
                System.out.println("2. Assists");
                System.out.println("3. Tackles");
                System.out.println("4. Yellow Cards");
                System.out.println("5. Red Cards");
                System.out.println("6. Passes Completed");
                System.out.println("7. Saves");
                System.out.println("8. Clean sheets");
                metric = wilson.nextInt();
                wilson.nextLine();
                System.out.println();

                System.out.println("Enter the Player's FIFA -ID:");
                fifaID = wilson.nextLine();
                while(fifaID.isEmpty()){
                    System.out.println("Please enter the player's FIFA -ID:");
                    fifaID = wilson.nextLine();
                }


                int outOfvariables =0;
                for(int i = 0; i<futballerz.size(); i++) {
                    Player playerAtindex = futballerz.get(i);
                    if (playerAtindex.getFIFAID().equals(fifaID)) {
                        outOfvariables = outOfvariables +1;
                        System.out.println("Enter number to update by:");
                        update = wilson.nextInt();
                        wilson.nextLine();
                        while(update<0){
                            System.out.println("Enter number to update by:");
                            update = wilson.nextInt();
                        }



                        if (metric == 1) {
                            System.out.println("Welcome to the Goals update Metric");
                            System.out.println();
                            playerAtindex.setGoals(playerAtindex.getGoals() + update);
                            System.out.println(" Metric successfully updated.");
                        } else if (metric == 2) {
                            playerAtindex.setAssists(playerAtindex.getAssists() + update);
                            System.out.println("Metric successful updated.");
                        } else if (metric == 3) {
                            playerAtindex.setTackles(playerAtindex.getTackles() + update);
                            System.out.println(" Metric successfully updated.");

                        } else if (metric == 4) {
                            playerAtindex.setYellowCard(playerAtindex.getYellowCard() + update);
                            System.out.println(" Metric successfully updated.");

                        } else if (metric == 5) {
                            playerAtindex.setRedCard(playerAtindex.getRedCard() + update);
                            System.out.println(" Metric successfully updated.");

                        } else if (metric == 6) {
                            playerAtindex.setPassesCompleted(playerAtindex.getPassesCompleted() + update);
                            System.out.println(" Metric successfully updated.");

                        } else if (metric == 7) {
                            playerAtindex.setSaves(playerAtindex.getSaves() + update);
                            System.out.println(" Metric successfully updated.");

                        } else if (metric == 8) {
                            playerAtindex.setCleansheets(playerAtindex.getCleansheets() + update);
                            System.out.println(" Metric successfully updated.");

                        } else {
                            System.out.println("Choose Correctly from the menu");
                            metric = wilson.nextInt();
                            wilson.nextLine();
                        }


                    }

                }
                if (outOfvariables==0){
                    System.out.println("Player not found. Please add player or type the correct fifa Id for the player.");

                   }
                System.out.println();
                System.out.println();




                //update stats
            }
            else if(menu == 3){
                if(futballerz.isEmpty()){
                    System.out.println("No player has been registered.");
                }
                else{
                    int rankz = 0;
                    while (rankz<1 || rankz>9) {
                        System.out.println("1. Golden Boot Ranking");
                        System.out.println("2. Assist Ranking");
                        System.out.println("3. Tackle Ranking");
                        System.out.println("4. Yellow Card Ranking");
                        System.out.println("5. Red Card Ranking");
                        System.out.println("6. Most passes Ranking");
                        System.out.println("7. Saves Ranking");
                        System.out.println("8. Cleansheet Ranking");
                        System.out.println("9. Overrall Best Player Ranking");


                        rankz = wilson.nextInt();
                        wilson.nextLine();
                        if (rankz == 1) {
                            FootballRanks.goalranks(futballerz);
                        } else if (rankz == 2) {
                            FootballRanks.assistranks(futballerz);
                        } else if (rankz == 3) {
                            FootballRanks.tacklesRanks(futballerz);
                        } else if (rankz == 4) {
                            FootballRanks.YellowCardsRanks(futballerz);
                        } else if (rankz == 5) {
                            FootballRanks.redCardsRanks(futballerz);
                        } else if (rankz == 6) {
                            FootballRanks.passesCompletedRanks(futballerz);
                        } else if (rankz == 7) {
                            FootballRanks.SavesRanks(futballerz);
                        } else if (rankz == 8) {
                            FootballRanks.cleanSheetRanks(futballerz);
                        } else if (rankz == 9) {
                            FootballRanks.overallRanks(futballerz);
                        } else {
                            System.out.println("Ranking not found. Please select again");
                            rankz = wilson.nextInt();
                            wilson.nextLine();
                        }
                    }
                }



                System.out.println();
                System.out.println();

            }


            else if(menu == 4){
                System.out.println("Thanks for using our system, Hope to see you again.");
                break;
            }
            System.out.println("1. Add Player");
            System.out.println("2. Update Stat");
            System.out.println("3. View Various Rankings");
            System.out.println("4. Exit");


            menu = wilson.nextInt();
            wilson.nextLine();




        }



    }

}
