/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package modelo;

import java.io.Serializable;

/**
 *
 * @author f_776
 */
public class Reading implements Serializable {
    private int id;
    private Yojijukugo yojijukugo;
    private String reading;

    public Reading(int id, Yojijukugo yojijukugo, String reading) {
        this.id = id;
        this.yojijukugo = yojijukugo;
        this.reading = reading;
    }

    public Reading() {
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Yojijukugo getYojijukugo() {
        return yojijukugo;
    }

    public void setYojijukugo(Yojijukugo yojijukugo) {
        this.yojijukugo = yojijukugo;
    }

    public String getReading() {
        return reading;
    }

    public void setReading(String reading) {
        this.reading = reading;
    }
    
    
}
