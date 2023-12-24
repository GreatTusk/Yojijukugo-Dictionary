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
public class SentenceExample implements Serializable {
    
    private Language language;
    private Yojijukugo yojijukugo;
    private String sentence;

    public SentenceExample() {
    }

    public SentenceExample(Language language, Yojijukugo yojijukugo, String sentence) {
        this.language = language;
        this.yojijukugo = yojijukugo;
        this.sentence = sentence;
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

    public String getSentence() {
        return sentence;
    }

    public void setSentence(String sentence) {
        this.sentence = sentence;
    }
    
    
}
