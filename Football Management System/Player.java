public class Player {
    //datafields
    protected String name;
    protected String club;
    protected String nationality;
    protected String FIFAID;
    protected String position;
    protected int goals;
    protected int assists;
    protected int tackles;
    protected int yellowCard;
    protected int redCard;
    protected int passesCompleted;
    protected int saves;
    protected int cleansheets;


    //constructor

    public Player(){

    }

    //constructor
    public Player (String name, String club,String nationality, String FIFAID, String position){
        this.name=name;
        this.club=club;
        this.nationality=nationality;
        this.FIFAID=FIFAID;
        this.position=position;
        this.goals = 0;
        this.assists= 0;
        this.tackles =0;
        this.yellowCard =0;
        this.redCard =0;
        this.passesCompleted =0;
        this.saves =0;
        this.cleansheets =0;

    }

    //getters
    public String getName(){
        return name;
    }

    public String getClub(){
        return club;
    }

    public String getNationality(){
        return nationality;
    }

    public String getFIFAID(){
        return FIFAID;
    }

    public String getPosition(){
        return position;
    }

    public int getGoals(){
        return goals;

    }

    public int getAssists(){
        return assists;
    }


    public int getYellowCard(){
        return yellowCard;
    }

    public int getRedCard(){
        return redCard;
    }

    public int getPassesCompleted(){
        return passesCompleted;
    }

    public int getSaves(){
        return saves;
    }
    //getters
    public int getTackles(){
        return tackles;
    }




    //setters
    public void setName(String name){
        this.name=name;
    }

    public void setClub(String club){
        this.club=club;
    }

    public void setPosition(String position){
        this.position=position;
    }

    public void setFIFAID(String FIFAID){
        this.FIFAID=FIFAID;
    }

    public void setNationality(String nationality){
        this.nationality=nationality;
    }


    public void setYellowCard(int yellowCard){
        this.yellowCard=yellowCard;
    }

    public void setRedCard(int redCard){
        this.redCard=redCard;
    }

    public void setPassesCompleted(int passesCompleted){
        this.passesCompleted=passesCompleted;
    }


    public void setTackles(int tackles){
        this.tackles=tackles;
    }



    public void setSaves(int saves) {
        this.saves = saves;
    }
    public void setCleansheets(int cleansheets){
        this.cleansheets=cleansheets;

    }



    public int getCleansheets(){
        return cleansheets;
    }

    public void setGoals(int goals){
        this.goals=goals;

    }
    public void setAssists(int assists){
        this.assists=assists;

    }



}
