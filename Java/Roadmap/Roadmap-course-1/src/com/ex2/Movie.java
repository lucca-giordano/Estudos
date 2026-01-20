package com.ex2;

public class Movie {

    String title;
    String rate;
    boolean watched;

    public Movie(String title, String rate, boolean watched) {
        this.title = title;
        this.rate = rate;
        this.watched = watched;
    }

    public void markAsWatched(){
        this.watched = true;
    }

    public void setRating(String rate){
        this.rate = rate;
    }

}
