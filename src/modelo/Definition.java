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
public class Definition implements Serializable {
    
    private Language language;
    private Yojijukugo yojijukugo;
    private String definition;

    public Definition() {
    }

    public Definition(Language language, Yojijukugo yojijukugo, String definition) {
        this.language = language;
        this.yojijukugo = yojijukugo;
        this.definition = definition;
    }

    public Language getLanguage() {
        return language;
    }

    public void setLanguage(Language language) {
        this.language = language;
    }

    public Yojijukugo getYojijukugo() {
        return yojijukugo;
    }

    public void setYojijukugo(Yojijukugo yojijukugo) {
        this.yojijukugo = yojijukugo;
    }

    public String getDefinition() {
        return definition;
    }

    public void setDefinition(String definition) {
        this.definition = definition;
    }
    
    
}
