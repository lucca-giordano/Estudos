package com.ex1;

public class Task {

    String title;
    String description;
    String startDate;
    String endDate;
    boolean isTaskComplete;

    public Task(String title, String description, String startDate, String endDate){
        this.title = title;
        this.description = description;
        this.startDate = startDate;
        this.endDate = endDate;
        this.isTaskComplete = false;

    }

    public void concluir(){
        this.isTaskComplete = true;
    }

}
